from .publisher import *


class StockTradingManager(Publisher):
    def __init__(self,stock_name:str, initial_price:float,notification_threshold: float):
        super().__init__()
        self.stock_prices = {}
        self.stock_name = stock_name
        self.initial_price = initial_price
        self.notification_threshold = notification_threshold

    def update_stock_price(self,new_price: float) -> None:
        self.stock_prices[self.stock_name] = new_price
        if new_price >= self.notification_threshold:
            self.notify_observers(self.stock_name,new_price)

