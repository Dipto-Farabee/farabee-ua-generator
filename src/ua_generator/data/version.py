"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0
"""
import random
from typing import Union, List

from src.ua_generator import exceptions


class Version:
    major: int = None
    minor: int = None
    build: int = None
    patch: int = None

    def __init__(self,
                 major: Union[int, tuple] = None,
                 minor: Union[int, tuple] = None,
                 build: Union[int, tuple] = None,
                 patch: Union[int, tuple] = None):
        self.major, self.minor, self.build, self.patch = map(
            lambda x:
            # https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
            random.randrange(*x) if isinstance(x, tuple) else x,
            (major, minor, build, patch)
        )

    def format(self, partitions=None, separator='.', trim_zero=False) -> str:
        versions = [self.major, self.minor, self.build, self.patch]

        if partitions is not None:
            versions = versions[:partitions]
        else:
            # Stop at None
            while versions[-1] is None:
                versions.pop()

        # None to zero
        versions = list(part or 0 for part in versions)

        if trim_zero:
            while versions[-1] == 0:
                versions.pop()

        return separator.join(str(part) for part in versions)

    # We use it for comparison. See: https://docs.python.org/3/reference/expressions.html#comparisons
    # TODO: Caching for best performance
    def to_tuple(self) -> tuple:
        return tuple(part or 0 for part in [self.major, self.minor, self.build, self.patch])

    def __eq__(self, other):
        return self.to_tuple() == other.to_tuple()

    def __ne__(self, other):
        return self.to_tuple() != other.to_tuple()

    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()

    def __gt__(self, other):
        return self.to_tuple() > other.to_tuple()

    def __le__(self, other):
        return self.to_tuple() <= other.to_tuple()

    def __ge__(self, other):
        return self.to_tuple() >= other.to_tuple()

    def __str__(self):
        return self.format()


class ChromiumVersion(Version):
    webkit: Version = None

    def __init__(self, version: Version, webkit: Version = Version(major=537, minor=36)):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.webkit = webkit


class AndroidVersion(Version):
    build_number: str = None
    platform_model: str = None

    def __init__(self, version: Version, build_numbers: tuple = None):
        super().__init__(version.major, version.minor, version.build, version.patch)
        if build_numbers is not None:
            self.build_number = random.choice(build_numbers)


class WindowsVersion(Version):
    ch_platform: Version = None

    def __init__(self, version: Version, ch_platform: Version):
        super().__init__(version.major, version.minor, version.build, version.patch)
        self.ch_platform = ch_platform


VERSION_TYPES = (
    Version,
    ChromiumVersion,
    AndroidVersion,
    WindowsVersion,
)


class VersionRange:
    min_version: Version = None
    max_version: Version = None

    def __init__(self, min_version: Union[Version, int] = None, max_version: Union[Version, int] = None):
        if min_version is None or max_version is None:
            raise exceptions.InvalidArgumentError("min_version and max_version must be specified")

        self.min_version = Version(major=min_version) if type(min_version) is int else min_version
        self.max_version = Version(major=max_version) if type(max_version) is int else max_version

        if self.max_version <= self.min_version:
            raise exceptions.InvalidArgumentError("max_version must be greater than min_version")

    def filter(self, versions: List[Version]) -> List[Version]:
        tmp_versions: List[Version] = []

        for version in versions:
            if self.min_version.major <= version.major <= self.max_version.major:
                tmp_versions.append(version)

        return tmp_versions
