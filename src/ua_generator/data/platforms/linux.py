"""
Farabee User-Agent Generator
Copyright: 2025 Dipto Farabee (github.com/Dipto-Farabee)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version
from ...options import Options

# https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/refs/
versions: List[Version] = [
    Version(major=5, minor=0, build=(0, 21)),
    Version(major=5, minor=1, build=(0, 21)),
    Version(major=5, minor=2, build=(0, 20)),
    Version(major=5, minor=3, build=(0, 18)),
    Version(major=5, minor=4, build=(0, 184)),
    Version(major=5, minor=5, build=(0, 19)),
    Version(major=5, minor=6, build=(0, 19)),
    Version(major=5, minor=7, build=(0, 19)),
    Version(major=5, minor=8, build=(0, 18)),
    Version(major=5, minor=9, build=(0, 16)),
    Version(major=5, minor=10, build=(0, 105)),
    Version(major=5, minor=11, build=(0, 22)),
    Version(major=5, minor=12, build=(0, 19)),
    Version(major=5, minor=13, build=(0, 19)),
    Version(major=5, minor=14, build=(0, 21)),
    Version(major=5, minor=15, build=(0, 103)),
    Version(major=5, minor=16, build=(0, 20)),
    Version(major=5, minor=17, build=(0, 15)),
    Version(major=5, minor=18, build=(0, 19)),
    Version(major=5, minor=19, build=(0, 17)),
    Version(major=6, minor=0, build=(0, 19)),
    Version(major=6, minor=1, build=(0, 78)),
    Version(major=6, minor=2, build=(0, 16)),
    Version(major=6, minor=3, build=(0, 13)),
    Version(major=6, minor=4, build=(0, 16)),
    Version(major=6, minor=5, build=(0, 13)),
    Version(major=6, minor=6, build=(0, 17)),
    Version(major=6, minor=7, build=(0, 5)),
]


def get_version(options: Options) -> Version:
    weights = None
    if options.weighted_versions:
        weights = [1.0] * len(versions)

    choice: List[Version] = random.choices(versions, weights=weights, k=1)
    return choice[0]
