from .strategies import *


class PricingManager:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def calculate_price(self, ride:RideDetails) -> float:
        return self.strategy.calculate_price(ride)