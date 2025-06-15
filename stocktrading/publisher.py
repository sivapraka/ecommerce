from .registry import *


class Publisher(ObserverRegistry):
    def __init__(self):
        self._observers = []

    @property
    def observers(self):
        return self._observers
    @observers.setter
    def observers(self, value):
        self._observers = value

    def add_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self,stock_name:str,new_price:float) -> None:
        for observer in self._observers:
            observer.send_notification(stock_name,new_price)

