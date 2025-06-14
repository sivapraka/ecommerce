from __future__ import annotations
import copy
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .cloneable import Cloneable


class ConfigurationType(Enum):
    BASIC = 'basic'
    ADVANCED = 'advanced'
    CUSTOM = 'custom'
    DEFAULT = 'default'



@dataclass
class Configuration(Cloneable["Configuration"]):
    theme_color:str
    auto_save: bool
    language: str
    dark_mode: bool
    font_size: int
    font_family: str
    type_: ConfigurationType

    def clone_object(self) -> Configuration:
        return copy.deepcopy(self)
