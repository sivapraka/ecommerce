from typing import Optional
from abc import ABC, abstractmethod

from customer.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        # Implementation goes here
        pass
