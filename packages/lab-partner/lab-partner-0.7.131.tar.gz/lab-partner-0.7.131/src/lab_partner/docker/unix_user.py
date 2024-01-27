import os


class UnixUser(object):
    def __init__(self):
        self._home = os.environ['HOME']
        self._username = os.environ['USER']
        self._uid = os.getuid()
        self._gid = os.getgid()

    @property
    def home(self) -> str:
        """Home directory of the current user

        :return: path to home directory
        """
        return self._home

    @property
    def username(self) -> str:
        """Name of the current user

        :return: current user name
        """
        return self._username

    @property
    def uid(self) -> int:
        """UID of the current user

        :return: current user UID
        """
        return self._uid

    @property
    def gid(self) -> int:
        """GID of the current user

        :return: current user GID
        """
        return self._gid

    def home_subdir(self, subdir: str) -> str:
        """
        Returns the path to a subdirectory under the user's home directory on the host system.
        :param subdir: Subdirectory (e.g. ".ssh")
        :return: Absolute path to home sub
        """
        return os.path.join(self._home, subdir)
