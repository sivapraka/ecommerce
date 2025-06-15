from dataclasses import dataclass
from enum import Enum


class GraphicType(Enum):
    JPEG = "jpeg"
    PNG = "png"
    SVG = "svg"


@dataclass
class Image:
    pass


@dataclass
class Graphic:
    type: GraphicType
    image: Image
    x: int
    y: int
    width: int
    height: int
    color: str


@dataclass
class GraphicIntrinsicState:
    image: str
    width: int
    height: int
    colour: str
    type: GraphicType


@dataclass
class GraphicExtrinsicState:
    x: int
    y:int
    intrinsic_state:GraphicIntrinsicState
