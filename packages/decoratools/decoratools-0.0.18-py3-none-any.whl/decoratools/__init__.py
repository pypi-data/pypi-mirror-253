from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from versioning.pep440 import NoVersion, Project

try:
    __version__ = version("decoratools")
except PackageNotFoundError:
    # package is not installed
    with Project(path=Path(__file__).parent) as project:
        try:
            __version__ = str(project.version())
        except NoVersion:
            __version__ = str(project.release(dev=0))
