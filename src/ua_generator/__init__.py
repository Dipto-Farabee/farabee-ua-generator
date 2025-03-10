"""
Farabee User-Agent Generator
Copyright: 2025 Dipto Farabee (github.com/Dipto-Farabee)
License: Apache License 2.0 
"""
from typing import Union

from . import user_agent, options as _options, data as _data


def generate(device: Union[_data.T_DEVICES, tuple, list, None] = None,
             platform: Union[_data.T_PLATFORMS, tuple, list, None] = None,
             browser: Union[_data.T_BROWSERS, tuple, list, None] = None,
             options: Union[_options.Options, None] = None) -> user_agent.UserAgent:
    return user_agent.UserAgent(device, platform, browser, options)
