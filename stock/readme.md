# Strategy Pattern for Stock Trading Indicators

## Problem Statement

You are tasked with refactoring a stock trading application. The application currently calculates various trading indicators such as moving averages, momentum, and volatility. These indicators are used to make decisions about buying, selling, or holding stocks. However, the current implementation relies on a single class, making it challenging to extend and maintain as new indicators are added. To address this, you need to refactor the application to use the Strategy pattern. This pattern allows you to encapsulate each trading indicator as a separate strategy and easily switch between them without modifying the core trading algorithm.

## Assignment

Your task is to refactor the `StockTradingManager` class to use the Strategy pattern for calculating trading indicators. An empty interface and dummy strategy classes have already been created for you. You have to add a method to the interface `calculate_indicator` and implement this method in the separate strategy classes for each trading indicator (Moving Averages, Momentum, and Volatility). Each strategy should define its calculation method for the respective indicator. The `StockTradingManager` class should utilize these strategies to calculate indicators based on the selected strategy type.


### Trading Indicator Calculations
1. **Moving Averages**: This indicator calculates the average of a stock's price and its previous price. It can help identify trends by smoothing out price fluctuations.

2. **Momentum**: Momentum is the difference between the current stock price and its previous price. It provides insights into the stock's rate of change.

3. **Volatility**: Volatility measures the magnitude of price fluctuations in a stock. It calculates the absolute difference between the current price and the previous price.

## Implementing the Strategy Pattern

1. **Complete the `TradingIndicatorStrategy` Interface**: Begin by adding methods to the `TradingIndicatorStrategy` interface. This interface should define a method `calculate_indicator` for calculating the indicator value.

2. **Implement Concrete Indicator Strategy Classes**: Complete the concrete classes that implement the `TradingIndicatorStrategy` interface. These classes represent different indicator strategies, including:
   - `MovingAverageStrategy`: Calculate the moving average of the stock price.
   - `VolatilityStrategy`: Calculate the volatility of the stock price based on the absolute difference between the current and previous prices.
   - `MomentumStrategy`: Calculate the momentum of the stock price based on the difference between the current and previous prices.

3. **Refactor the `StockTradingManager` Class**: Refactor the existing `StockTradingManager` class by removing the hardcoded indicator logic and instead delegating the indicator calculation to the selected strategy. The `StockTradingManager` class should now use composition to hold an instance of the selected strategy. You need to accept the strategy as a parameter in the `StockTradingManager` constructor and use it to calculate the indicator.

4. **Test Your Refactored Code**: Write test cases to ensure that the refactored code produces accurate calculations for each strategy. You should test different scenarios to verify that each strategy behaves as expected.

## Instructions

Refactor the `StockTradingManager` class by implementing the Strategy pattern:
   - Add a method `calculate_indicator` to the `TradingIndicatorStrategy` interface.
   - Implement separate indicator strategy classes for moving averages, momentum, and volatility.
   - Add a field to the `StockTradingManager` class to hold the selected strategy.
   - Pass the strategy as a parameter to the `StockTradingManager` constructor and use it to calculate the indicator value.
