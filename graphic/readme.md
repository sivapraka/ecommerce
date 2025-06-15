Flyweight Pattern for a graphical editing software
Problem Statement
You are working on a graphical editing software. The application must support rendering text with different fonts, sizes, and colors. The application must also support rendering images with different dimensions and formats. Joe is concerned about the memory overhead of creating multiple text and image objects with the same state.

Assignment
Your task is to implement the Flyweight pattern to optimize the memory usage of graphical elements in the editing software. The Flyweight pattern aims to share a common state between multiple objects to reduce memory consumption.

Task 1—Intrinsic and Extrinsic State Separation
In the Flyweight pattern, objects are split into intrinsic state (shared and independent of the context) and extrinsic state (variable and dependent on the context). Your task is to refactor the initial Graphic class into two separate classes: GraphicIntrinsicState and GraphicExtrinsicState.

GraphicIntrinsicState class:

Complete the class named GraphicIntrinsicState with appropriate fields to represent the intrinsic state of a graphic element. You have been given an empty class.
Do not change the name of the fields as the test cases depend on the field names.
GraphicExtrinsicState class:

Complete the class named GraphicExtrinsicState with appropriate fields to represent the extrinsic state of a graphic element. You have been given an empty class.
Make sure to add a reference called intrinsic_state to the GraphicIntrinsicState class in the GraphicExtrinsicState class.
Do not change the name of the fields as the test cases depend on the field names.
Task 2—Implementing the registry pattern
To make the storage and usability of the flyweight easier, implement the registry pattern

The interface called FlyweightRegistry has been provided. You need to implement these methods in the FlyweightRegistryImpl class.
The class should store the flyweight and fetch the relevant flyweight based on the type.
Instructions
Implement the GraphicIntrinsicState and GraphicExtrinsicState by breaking the original class into intrinsic and extrinsic state.
Ensure that the names of the fields in the GraphicIntrinsicState and GraphicExtrinsicState classes are not changed.
Implement the registry interface's FlyweightRegistry to add and get flyweight methods.
Run the provided test cases in the GraphicTest class to verify the correctness of your implementation. You are not required to edit the test cases themselves.