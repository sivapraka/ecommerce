from .model import *


class StockTradingManager:
    def __init__(self, strategy: TradingStrategyType):
        self.strategy = strategy

    def calculate_indicator (self, ride:Stock) -> float:
        return self.strategy.calculate_indicator(ride)