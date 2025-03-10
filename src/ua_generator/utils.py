"""
Farabee User-Agent Generator
Copyright: 2025 Dipto Farabee (github.com/Dipto-Farabee)
License: Apache License 2.0 
"""
import random
from typing import Union


def choice(t: Union[str, tuple, list, None]) -> Union[str, None]:
    if type(t) is str:
        return t
    if type(t) is tuple or type(t) is list:
        return random.choice(t)

    return None
