import asyncio
import asyncio.subprocess as aio_subprocess
from dataclasses import dataclass
import json
import logging
import os
from typing import Mapping, Any, Optional, Dict

from panza import metadata
from panza.errors import InspectionError, JobExecutionBackendError, JobExecutionTimeout

from panza.internals.workspace import BaseJobWorkspaceHandle, EXECUTOR_WORKSPACE_ROOT, WorkspaceLayout
from panza.internals.pipe_stream import AsyncPipeStream
from panza.internals.result_serialization import load_result

from . import Backend
from ._docker_builder import _DockerImageBuilderBackend
from ._utils import check_subprocess_exec, subprocess_exec, generate_unique_name


@dataclass
class IgniteConfiguration:
    base_image: str = f"etnajawa/panza-base:{metadata.__version__}-ignite"
    always_pull: bool = False
    max_wait_time: float = 10.0
    memory: str = "2GB"
    size: str = "10GB"
    cpus: int = 1


class VMFileCopyError(JobExecutionBackendError):
    def __init__(self, src: str, dest: str):
        self.src = src
        self.dest = dest

    def __str__(self):
        return f"unable to copy file {self.src} to {self.dest}"


class VMStartupError(JobExecutionBackendError):
    def __str__(self):
        return "unable to start VM"


async def _copy_file(src: str, dest: str):
    return_code = await subprocess_exec("ignite", "cp", src, dest)
    if return_code != 0:
        raise VMFileCopyError(src, dest)


async def _create_vm(name: str, environment_tag: str, config):
    return_code = await subprocess_exec(
        "ignite", "run", environment_tag,
        "--runtime", "docker",
        "--name", name,
        "--cpus", str(config.cpus),
        "--memory", config.memory,
        "--size", config.size,
        "--ssh", "--quiet",
    )
    if return_code != 0:
        raise VMStartupError


class IgniteBackend(Backend, _DockerImageBuilderBackend):
    def __init__(self, config: IgniteConfiguration):
        self.config: IgniteConfiguration = config
        self.logger = logging.getLogger("panza.ignite")

    async def build_environment(self, tag: str, job: BaseJobWorkspaceHandle):
        await self._build_environment(tag, job)

    def _configure_job_directory(self, context: Mapping[str, Any], workspace):
        os.mkdir(workspace.work_directory)

        with open(workspace.context_file, 'w') as context_file:
            json.dump(context, context_file)

    async def _destroy_vm(self, vm_name: str):
        await subprocess_exec("ignite", "kill", vm_name)
        await subprocess_exec("ignite", "rm", vm_name)

    async def _destroy_ignite_environment(self, environment_tag: str):
        # This is necessary because ignite actually copies images from Docker into its own cache
        # Thus, once an image has been imported, ignite reuses its cached version rather than checking if the
        # original image has changed in Docker
        await subprocess_exec("ignite", "image", "rm", environment_tag)

    async def run(
            self,
            context: Mapping[str, Any],
            environment_tag: str,
            job: BaseJobWorkspaceHandle,
            timeout: Optional[float],
    ) -> Dict[str, Any]:
        self._configure_job_directory(context, job.workspace)

        vm_name = generate_unique_name()

        try:
            self.logger.debug(f"Starting up VM with name {vm_name}...")
            await _create_vm(vm_name, environment_tag, self.config)

            self.logger.debug(f"Copying workspace to the VM...")
            await _copy_file(src=job.workspace.root, dest=f"{vm_name}:{EXECUTOR_WORKSPACE_ROOT}")

            async with check_subprocess_exec(
                    "ignite", "exec", vm_name, "panza_executor",
                    stderr=aio_subprocess.STDOUT,
                    stdout=aio_subprocess.PIPE,
            ) as proc:
                self.logger.debug("Inspection output:")
                try:
                    async for line in AsyncPipeStream(proc.stdout).iter_lines(with_timeout=timeout):
                        self.logger.debug("  " + line.rstrip())
                except asyncio.TimeoutError:
                    proc.kill()
                    raise JobExecutionTimeout(timeout)

            if proc.returncode != 0:
                raise InspectionError(f"inspector process exited with error status {proc.returncode}")

            self.logger.debug(f"Retrieving job result from the VM...")
            await _copy_file(
                src=f"{vm_name}:{WorkspaceLayout(EXECUTOR_WORKSPACE_ROOT).result_file}",
                dest=job.workspace.result_file
            )
        finally:
            await self._destroy_vm(vm_name)
            await self._destroy_ignite_environment(environment_tag)

        return load_result(job.workspace.result_file)
