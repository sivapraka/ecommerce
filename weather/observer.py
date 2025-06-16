from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update_weather_conditions(self,value:float)->None:
        pass
    @abstractmethod
    def trigger(self)->None:
        pass


class HumidityService(Observer):
    def trigger_humidity(self, value: float) -> None:
        print(f"Triggering humidity event with value {value}")


class TemperatureService(Observer):
    def trigger_temperature(self, value: float) -> None:
        print(f"Triggering temperature event with value {value}")


class PressureService(Observer):
    def trigger_pressure(self, value: float) -> None:
        print(f"Triggering pressure event with value {value}")

