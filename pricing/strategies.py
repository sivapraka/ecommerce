from abc import ABC, abstractmethod

from .model import *


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, ride: RideDetails) -> float:
        pass


class DistanceBasedPricingStrategy(PricingStrategy):
    BASE_FARE = 5.0
    RATE_PER_KM = 2.0

    def calculate_price(self,ride:RideDetails) -> float:
        return self.BASE_FARE + self.RATE_PER_KM * ride.distance


class TimeBasedPricingStrategy(PricingStrategy):
    BASE_FARE = 5.0
    RATE_PER_MIN = 0.5

    def calculate_price(self,ride:RideDetails) -> float:
        return self.BASE_FARE + self.RATE_PER_MIN * ride.duration


class SurgePricingStrategy(PricingStrategy):
    SURGE_MULTIPLIER = 2.0

    def calculate_price(self, ride:RideDetails) -> float:
        return ride.base_fare * self.SURGE_MULTIPLIER
