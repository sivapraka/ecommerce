from typing import Optional
from abc import ABC, abstractmethod
from .user import User, UserType


class UserPrototypeRegistry(ABC):
    @abstractmethod
    def add_prototype(self, user: User) -> None:
        pass

    @abstractmethod
    def get_prototype(self, type_: UserType) -> Optional[User]:
        pass

    @abstractmethod
    def clone(self, type_: UserType) -> Optional[User]:
        pass
