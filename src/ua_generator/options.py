"""
Farabee User-Agent Generator
Copyright: 2025 Dipto Farabee (github.com/Dipto-Farabee)
License: Apache License 2.0 
"""
import typing

from .data.version import VersionRange


class Options:
    weighted_versions: bool = False
    version_ranges: typing.Dict[str, VersionRange] = None

    def __init__(self, weighted_versions: bool = False, version_ranges: typing.Dict[str, VersionRange] = None):
        self.weighted_versions = weighted_versions
        if version_ranges is not None:
            self.version_ranges = version_ranges

    def __repr__(self):
        return f"Options(weighted_versions={self.weighted_versions}, version_ranges={self.version_ranges})"
