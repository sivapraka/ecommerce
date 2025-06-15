from dataclasses import dataclass
from enum import Enum


class Colour(Enum):
    WHITE = "white"
    BLACK = "black"


@dataclass
class ChessUser:
    name: str
    age: int
    gender: str
    email: str
    phoneNumber: str
    colour: Colour
    currentGameStreak: int
    photo: bytes


@dataclass
class UserIntrinsicState:
    name: str
    age: int
    gender: str
    email: str
    phone_number: str
    photo: str

@dataclass
class UserExtrinsicState:
    colour: Colour
    current_game_streak: int
    intrinsic_state: UserIntrinsicState