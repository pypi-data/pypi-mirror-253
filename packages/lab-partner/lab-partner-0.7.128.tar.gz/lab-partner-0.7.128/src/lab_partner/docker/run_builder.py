import os
import logging
from pathlib import Path
from typing import List, Optional
from .unix_user import UnixUser



logger = logging.getLogger(__name__)



class InvalidDockerOptionConfiguration(Exception):
    pass


class DockerRunOptions(object):
    """
    This class helps build up a list of options for the invocation of Docker.
    """
    def __init__(self):
        self._options = set()
        self._user_info = UnixUser()

    def with_init(self) -> 'DockerRunOptions':
        self._options.add('--init')
        return self

    def with_remove_on_exit(self) -> 'DockerRunOptions':
        self._options.add(f'--rm')
        return self

    def with_name(self, name: str) -> 'DockerRunOptions':
        self._options.add(f'--name {name}')
        return self

    def with_hostname(self, hostname: str) -> 'DockerRunOptions':
        self._options.add(f'--name {hostname}')
        return self

    def with_current_user(self) -> 'DockerRunOptions':
        return self.with_user(self._user_info.uid, self._user_info.gid)
    
    def with_root_user(self) -> 'DockerRunOptions':
        return self.with_user(0, 0)

    def with_user(self, uid: int, gid: int) -> 'DockerRunOptions':
        """Run container as a specific user

        :param uid: UID of the user to run as
        :param gid: GID of the user to run as
        :return: self
        """
        self._options.add(f'--user {uid}:{gid}')
        return self

    def with_privileged(self) -> 'DockerRunOptions':
        self._options.add('--privileged')
        return self
    
    def with_host_ipc(self) -> 'DockerRunOptions':
        self._options.add('--ipc=host')
        return self

    def with_tty(self) -> 'DockerRunOptions':
        if self._is_daemon():
            raise InvalidDockerOptionConfiguration('Launch a tty is not compatible with daemon mode')
        self._options.add('-it')
        return self

    def _is_tty(self) -> bool:
        return '-it' in self._options

    def with_daemon(self) -> 'DockerRunOptions':
        if self._is_tty():
            raise InvalidDockerOptionConfiguration('Launching as a daemon is not compatible with tty mode')
        self._options.add('-d')
        return self

    def _is_daemon(self) -> bool:
        return '-d' in self._options

    def with_network(self, network_name: str) -> 'DockerRunOptions':
        self._options.add(f'--network={network_name}')
        return self

    def with_workdir(self, workdir: str) -> 'DockerRunOptions':
        self._options.add(f'--workdir={workdir}')
        return self

    def with_env(self, key: str, value: Optional[str] = None) -> 'DockerRunOptions':
        """
        Adds an environment value option to the Docker command line, assuming both the
        key and value are non-empty.
        :param key: Environment variable name
        :param value: Environment variable value
        :return: self
        """
        if key and value:
            self._options.add(f'-e {key}={value}')
        elif key:
            self._options.add(f'-e {key}')
        return self

    def with_mount_user_run(self) -> 'DockerRunOptions':
        self._options.add(f'-v /run/user/{self._user_info.uid}/:/run/user/{self._user_info.uid}/')
        return self

    def with_mount_home(self) -> 'DockerRunOptions':
        self._options.add(f'-v {self._user_info.home}:{self._user_info.home}')
        return self

    def with_home_dir_bind_mount(self, source: str, target: str, validate_source_exists: bool = True) -> 'DockerRunOptions':
        source_in_home = self._user_info.home_subdir(source)
        if source and target and self._path_exists(source_in_home, validate_source_exists):
            self._options.add(f'-v {source_in_home}:{target}')
        else:
            logger.warning(f'Requested HOME mount that does not exist: {source_in_home}')
        return self

    def with_bind_mount(self, source: str, target: str) -> 'DockerRunOptions':
        """
        Adds an option to bind mount a host volume
        :param source: Source host path to be mounted
        :param target: Target path inside container to attach the mount
        :return: self
        """
        self._options.add(f'-v {source}:{target}')
        return self

    def with_named_volume(self, name: str, target: str) -> 'DockerRunOptions':
        self._options.add(f'--mount type=volume,src={name},dst={target}')
        return self

    def with_port_mapping(self, external_port: int, internal_port: int) -> 'DockerRunOptions':
        self._options.add(f'-p {external_port}:{internal_port}')
        return self
    
    def with_entrypoint(self, entrypoint: str) -> 'DockerRunOptions':
        self._options.add(f'--entrypoint={entrypoint}')
        return self

    def build(self) -> str:
        """
        Builds the accumulated options into a space-separated string.
        :return: String containing all the options.
        """
        return ' '.join(self._options)

    @staticmethod
    def _path_exists(path: str, should_validate: bool) -> bool:
        """
        Method used to check for the existence of a source path
        :param path: Path to be checked
        :param should_validate: Whether we should really check.  If False, the method
        will return True regardless of whether the path exists.
        :return:
        """
        if not should_validate:
            return True
        else:
            return Path(path).exists()


class DockerRunBuilder(object):
    def __init__(self, image_name: str, command: str = ''):
        self._image_name = image_name
        self._command = command
        self._options = DockerRunOptions()

    def options(self):
        return self._options

    def build(self) -> str:
        return f'docker run \
                {self._options.build()} \
                {self._image_name} \
                {self._command}'
