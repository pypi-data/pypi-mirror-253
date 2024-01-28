import sys
from importlib import metadata


def lab_version():
    return metadata.version('lab-partner')


def is_linux() -> bool:
    """
    Check current platform is Linux
    :return: True on Linux
    """
    return sys.platform in ('linux',)


def is_supported_platform() -> bool:
    """
    Check current platform is MacOS or Linux
    :return: True on MacOS or Linux
    """
    return sys.platform in ('darwin', 'linux')
