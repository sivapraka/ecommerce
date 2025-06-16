# Observer Pattern for Weather Monitoring System

## Problem Statement
You are developing a weather monitoring system that collects data from various sensors such as temperature, humidity, and pressure sensors. When any sensor reading goes beyond a predefined threshold, you need to trigger different types of processes specific to the type of the sensor. For example, if it is a temperature sensor, you need to send an alert to the air conditioning system. If it is a humidity sensor, you need to send an alert to the dehumidifier system. To achieve this, you want to implement the Observer pattern, allowing the sensors to notify the monitoring system when the sensor readings cross the threshold.


## Assignment
Your goal is to implement the Observer pattern to refactor the existing `WeatherMonitoringApplication` class. The current class handles weather condition updates and notifications. `Observer` classes (e.g., `TemperatureService`, `PressureService`, `HumidityService`) need to be notified when any of the weather readings go beyond their respective thresholds.

You need to implement the observer pattern by first defining a method to notify observers in the `Observer` abstract class. Then, you need to implement the `Observer` interface and modify the observer classes to receive notifications. The observer side of the pattern is ready. 

To implement the publisher side, the registry interface is provided to you through the `ObserverRegistry` abstract class. You need to implement the methods required by this class in the `Publisher` class. The `Publisher` class is a contract that defines the methods that a class can use to add, remove, and notify observers. The `WeatherMonitoringApplication` class will implement the `Publisher` class to notify observers when the weather readings cross the threshold.

## Implementing the Observer Pattern

1. **Review the original class**: Study the `WeatherMonitoringApplication` class and its dependencies. Understand how it currently handles weather condition updates and triggers further actions.

2. **Complete the observer interface**: Design an interface named `Observer` with a method `trigger` that accepts the value as an argument. Add this method to the already provided `Observer` abstract class. This method will be used to notify observers when the weather readings cross the threshold.

3. **Modify the concrete observers**: Observer classes (such as `TemperatureService`, `PressureService`, `HumidityService`) will implement the `Observer` interface to receive notifications. Update the existing methods in these classes to match the new interface method signature.

4. **Implement the publisher class**: You have been provided with an empty `Publisher` class. The publisher class is a contract that defines the methods that a class can use to add, remove, and notify observers. The `currently` class will implement the `Publisher` class to notify observers when the weather readings cross the threshold. Your task is to first inherit the `ObserverRegistry` abstract class and then implement the methods defined by this class in the `Publisher` class. The `ObserverRegistry` class provides methods to add, remove, and notify observers. You just need to implement these methods in the `Publisher` class.

5. **Modify the publisher**: Refactor the `WeatherMonitoringApplication` class as required to implement the `Publisher` class. The `WeatherMonitoringApplication` class should now be able to add, remove, and notify observers. Also modify the method `update_weather_conditions` to notify observers when the weather readings cross the threshold.

6. **Test your implementation**: Run the provided test cases in the `WeatherMonitoringApplicationTest` class to ensure that your observer pattern implementation is correct. These test cases will check if observers are being notified correctly and if the `WeatherMonitoringApplication` behaves as expected.

## Instructions
1. Add `trigger` method to the `Observer` abstract class.
2. Implement the `Observer` interface in the observer classes (`TemperatureService`, `PressureService`, `HumidityService`) to receive notifications.
3. Inherit the `ObserverRegistry` abstract class and implement the methods in the `Publisher` class to add, remove, and notify observers.
4. Modify the `WeatherMonitoringApplication` class to implement the `Publisher` class and notify observers when the weather readings cross the threshold.
5. Run the provided test cases in the `WeatherMonitoringApplicationTest` class to validate the correctness of your observer pattern implementation. Ensure that observers are being notified correctly and that the `WeatherMonitoringApplication` behaves as expected.