from enum import Enum
from dataclasses import dataclass

class PricingType(Enum):
    DISTANCE_BASED = 1
    TIME_BASED = 2
    SURGE = 3

@dataclass
class RideDetails:
    def __init__(self):
        self.base_fare = None

    distance: float
    duration: float