from __future__ import annotations

import copy
from dataclasses import dataclass
from enum import Enum

from .cloneable import Cloneable


class UserType(Enum):
    BASIC = "basic"
    PREMIUM = "premium"
    ADMIN = "admin"


@dataclass
class User(Cloneable):
    user_id: int
    username: str
    email: str
    display_name: str
    age: int
    type_: UserType

    def clone_object(self) -> User:
        return copy.deepcopy(self)

    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, type={self.type_})"