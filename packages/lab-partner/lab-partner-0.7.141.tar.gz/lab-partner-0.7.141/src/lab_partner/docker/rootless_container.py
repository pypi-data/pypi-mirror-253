import os
import logging
import sys
import time
import itertools
from subprocess import CalledProcessError
from typing import Tuple, Dict

from .daemon_info import DockerDaemonInfo
from .run_builder import DockerRunBuilder
from ..process_utils import run_process, run_process_quiet
from ..metadata_utils import lab_version


logger = logging.getLogger(__name__)


XDG_RUNTIME_DIR = os.environ['XDG_RUNTIME_DIR']
ROOTLESS_DOCKER_IMAGE = f'enclarify/lab-partner-dind-rootless:{lab_version()}'
ROOTLESS_DOCKER_NAME = 'lab-rootless-docker'
ROOTLESS_DOCKER_URL = f'unix://{XDG_RUNTIME_DIR}/docker.sock'

LAB_ROOTLESS_STORAGE = 'lab-rootless-storage'
LAB_ROOTLESS_USER_STORAGE = 'lab-rootless-user-storage'
LAB_CICD_ARTIFACT_STORAGE = 'lab-cicd-artifact-storage'

WAITING_ANIMATION_FRAMES = itertools.cycle(['|', '/', '—', '\\'])


class RootlessDockerContainer(object):
    """

    """
    def __init__(self, container_name: str, daemon_info: DockerDaemonInfo):
        self.container_name = container_name
        self._daemon_info = daemon_info

    def does_rootless_container_exist(self) -> bool:
        for c in self._daemon_info.containers:
            if self.container_name == c['Names']:
                return True
        return False

    def is_rootless_container_running(self) -> bool:
        for c in self._daemon_info.containers:
            if self.container_name == c['Names'] and 'running' == c['State']:
                return True
        return False

    def is_rootless_container_not_running(self) -> bool:
        for c in self._daemon_info.containers:
            if self.container_name == c['Names'] and 'running' != c['State']:
                return True
        return False

    def start_rootless_container(self, workspace_path: str, network_name: str) -> DockerDaemonInfo:
        if self.is_rootless_container_running():
            logger.info(f'Rootless container {self.container_name}')
            return DockerDaemonInfo.build_with_docker_host(ROOTLESS_DOCKER_URL)
        else:
            logger.info(f'Starting rootless container. It can take a couple minutes to start')

        if self.is_rootless_container_not_running():
            logger.info(f'Killing dead rootless container {self.container_name}')
            for log_line in run_process(f'docker rm -f {self.container_name}'):
                logger.info(log_line)

        self._create_user_named_volume(LAB_CICD_ARTIFACT_STORAGE)

        run_rootless_docker_cmd = DockerRunBuilder(ROOTLESS_DOCKER_IMAGE)
        run_rootless_docker_cmd.options() \
            .with_name(self.container_name) \
            .with_hostname(self.container_name) \
            .with_privileged() \
            .with_host_ipc() \
            .with_daemon() \
            .with_current_user() \
            .with_env('DOCKER_TLS_CERTDIR', '') \
            .with_env('POOL_BASE', '172.28.0.0/16') \
            .with_env('POOL_SIZE', '21') \
            .with_port_mapping(80, 80) \
            .with_bind_mount(workspace_path, workspace_path) \
            .with_bind_mount('/tmp', '/tmp') \
            .with_bind_mount('/dev', '/dev') \
            .with_named_volume(LAB_ROOTLESS_STORAGE, '/var/lib/docker') \
            .with_named_volume(LAB_ROOTLESS_USER_STORAGE, '/home/rootless/.local/share/docker') \
            .with_named_volume(LAB_CICD_ARTIFACT_STORAGE, '/opt/lab/cicd/artifacts') \
            .with_mount_home() \
            .with_mount_user_run() \
            .with_network(network_name)

        for log_line in run_process(run_rootless_docker_cmd.build()):
            logger.info(log_line)

        self._wait_for_rootless()

        docker_daemon_info = DockerDaemonInfo.build_with_docker_host(ROOTLESS_DOCKER_URL)
        docker_daemon_info.create_network(network_name)
        return docker_daemon_info
    
    def _create_user_named_volume(self, name: str) -> None:
        """Create a user accessible named volumed

        Named volumes get create as root. This changes the ownership
        to be "rootless" in order for it to properly get mapped to
        the host user

        :param name: name of the named volume to create
        """
        if self._daemon_info.create_volume(name):
            fix_volume_permissions = DockerRunBuilder(ROOTLESS_DOCKER_IMAGE, '/bin/sh -c "chown -R rootless:rootless /data"')
            fix_volume_permissions.options() \
                .with_name(f'fix-volume-{name}') \
                .with_hostname(f'fix-volume-{name}') \
                .with_named_volume(name, '/data') \
                .with_entrypoint('') \
                .with_root_user() \
                .with_remove_on_exit()
            
            for log_line in run_process(fix_volume_permissions.build()):
                logger.info(log_line)

    def _wait_for_rootless(self, timeout: int = 120) -> None:
        start_time = time.perf_counter()
        while True:
            if not self.is_rootless_container_running():
                time.sleep(1)
                continue
            try:
                run_process_quiet('docker info', {'DOCKER_HOST': ROOTLESS_DOCKER_URL})
                break
            except CalledProcessError as ex:
                elapsed_time = time.perf_counter() - start_time
                sys.stdout.write(f'{next(WAITING_ANIMATION_FRAMES)} Waiting for rootless docker to start\r')
                sys.stdout.flush()
                if elapsed_time >= timeout:
                    raise TimeoutError(f'Timeout waiting for rootless docker after {timeout} seconds', ex)
                time.sleep(.1)
