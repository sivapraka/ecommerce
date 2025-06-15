# Strategy Pattern for Video Streaming Quality Adjustment

## Problem Statement

You are developing a video streaming platform that offers different streaming qualities, such as low, standard, and high definition. The platform should dynamically adjust the streaming quality based on the user's network conditions to ensure smooth playback. Additionally, more quality adjustment algorithms may be added in the future. Your task is to implement this dynamic quality adjustment system using the Strategy pattern.

## Assignment

Your task is to refactor the `VideoStreamingManager` class to use the Strategy pattern for adjusting the video based on the requested quality. An empty interface and dummy strategy classes have already been created for you. You have to add a method to the interface `adjust_quality` and implement this method in the separate strategy classes for each video quality. Each strategy should define its logic for the respective quality. The `VideoStreamingManager` class should utilize these strategies to process the adjustments based on the selected strategy type.

## Implementing the Strategy Pattern

1. **Complete the `QualityAdjustmentStrategy` Interface**: Begin by adding methods to the `QualityAdjustmentStrategy` interface. This interface should define a method `adjust_quality` for performing the quality adjustment based on the selected strategy.

2. **Implement Concrete Indicator Strategy Classes**: Complete the concrete classes that implement the `QualityAdjustmentStrategy` interface. These classes represent different quality adjustment strategies, such as low, standard, and high definition. Each class should implement the `adjust_quality` method to define the logic for adjusting the video quality based on the selected strategy.

3. **Refactor the `VideoStreamingManager` Class**: Refactor the existing `VideoStreamingManager` class by removing the hardcoded adjustment logic and instead delegating the processing to the selected strategy. The `VideoStreamingManager` class should now use composition to hold an instance of the selected strategy. You need to accept the strategy as a parameter in the `VideoStreamingManager` constructor and use it to adjust the video quality.

4. **Test Your Refactored Code**: Write test cases to ensure that the refactored code produces accurate results for each strategy. You should test different scenarios to verify that each strategy behaves as expected.

## Instructions

Refactor the `VideoStreamingManager` class by implementing the Strategy pattern:
   - Add a method `adjust_quality` to the `QualityAdjustmentStrategy` interface.
   - Implement the `adjust_quality` method in the concrete strategy classes for low, standard, and high definition.
   - Add a field to the `VideoStreamingManager` class to hold the selected strategy.
   - Pass the strategy as a parameter to the `VideoStreamingManager` constructor and use it to adjust the video quality.
