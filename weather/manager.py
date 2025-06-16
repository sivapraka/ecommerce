from .publisher import Publisher

class WeatherMonitoringApplication(Publisher):
    def __init__(self, initial_temperature: float,initial_humidity: float,initial_pressure: float, temperature_threshold: float,humidity_threshold: float, pressure_threshold: float,):
        super().__init__()
        self.initial_temperature = initial_temperature
        self.initial_humidity = initial_humidity
        self.initial_pressure = initial_pressure
        self.temperature_threshold = temperature_threshold
        self.humidity_threshold = humidity_threshold
        self.pressure_threshold = pressure_threshold


    def update_weather_conditions(
        self,
        temperature: float,
        humidity: float,
        pressure: float
    ) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        if temperature > self.temperature_threshold:
            self.notify_observers(temperature)

        if humidity > self.humidity_threshold:
            self.notify_observers(humidity)

        if pressure > self.pressure_threshold:
            self.notify_observers(pressure)

