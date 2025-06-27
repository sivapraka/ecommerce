from hotel.models.base_model import BaseModel
from hotel.models.user_type import UserType


class User(BaseModel):
    name: str
    password: str
    phone: str
    user_type: UserType

    def __init__(self, name=None, password=None, phone=None, user_type=UserType.CUSTOMER):
        super().__init__()
        self.name = name
        self.password = password
        self.phone = phone
        self.user_type = user_type
