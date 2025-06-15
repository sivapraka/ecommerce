# Observer Pattern for Task Management Application

## Problem Statement
You are building a task management application where users can create tasks and assign them to different team members. To enhance the user experience, Joe, a developer on your team, wants to implement a feature where team members receive notifications whenever they are assigned a new task. These notifications should be sent through various communication channels, such as in-app alerts, emails, and Slack messages. Joe believes that implementing the Observer pattern will provide a flexible and maintainable solution for this requirement.

## Assignment
Your task is to implement the Observer pattern to create a flexible notification system for the task management application. The `TaskManager` class handles task assignments, and various observer classes (e.g., `InAppAlertService`, `EmailService`, `SlackService`) need to be notified when a new task is assigned to a team member.

You need to implement the observer pattern by first defining a method to notify observers in the `Observer` abstract class. Then, you need to implement the `Observer` interface and modify the observer classes to receive notifications. The observer side of the pattern is ready. 

To implement the publisher side, the registry interface is provided to you through the `ObserverRegistry` abstract class. You need to implement the methods required by this class in the `Publisher` class. The `Publisher` class is a contract that defines the methods that a class can use to add, remove, and notify observers. The `TaskManager` class will implement the `Publisher` class to notify observers when a new task is assigned to a team member.

## Implementing the Observer Pattern

1. **Review the original class**: Study the `TaskManager` class and its dependencies. Understand how it currently handles task assignments and sends notifications.

2. **Complete the observer interface**: Design an interface named `Observer` with a method `send_notification` that accepts the task name and team member as arguments. Add this method to the already provided `Observer` abstract class. This method will be used to notify observers when a new task is assigned to a team member.

3. **Modify the concrete observers**: Observer classes (such as `EmailService`, `SlackService`, `AppService`) will implement the `Observer` interface to receive notifications. Update the existing methods in these classes to match the new interface method signature.

4. **Implement the publisher class**: You have been provided with an empty `Publisher` class. The publisher class is a contract that defines the methods that a class can use to add, remove, and notify observers. The `TaskManager` class will implement the `Publisher` class to notify observers when a new task is assigned to a team member. Your task is to first inherit the `ObserverRegistry` abstract class and then implement the methods defined by this class in the `Publisher` class. The `ObserverRegistry` class provides methods to add, remove, and notify observers. You just need to implement these methods in the `Publisher` class. 

5. **Modify the publisher**: Refactor the `TaskManager` class as required to implement the `Publisher` class. The `TaskManager` class should now be able to add, remove, and notify observers. Also modify the method `assign_task` to notify observers when a new task is assigned to a team member.

6. **Test your implementation**: Run the provided test cases in the `TaskManagerTest` class to ensure that your observer pattern implementation is correct. These test cases will check if observers are being notified correctly and if the `TaskManager` behaves as expected.

## Instructions
1. Add `send_notification` method to the `Observer` abstract class.
2. Implement the `Observer` interface in the observer classes (`EmailService`, `SlackService`, `AppService`) to receive notifications.
3. Inherit the `ObserverRegistry` abstract class and implement the methods in the `Publisher` class to add, remove, and notify observers.
4. Modify the `TaskManager` class to implement the `Publisher` class and notify observers when a new task is assigned to a team member.
5. Run the provided test cases in the `TaskManagerTest` class to validate the correctness of your observer pattern implementation. Ensure that observers are being notified correctly and that the `TaskManager` behaves as expected.