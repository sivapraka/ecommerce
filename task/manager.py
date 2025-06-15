from .publisher import Publisher


class TaskManager(Publisher):

    def __init__(self):
        super().__init__()
        self.tasks = {}

    def assign_task(self, task_name: int, team_member: int) -> None:
        self.tasks[task_name] = task_name
        self.tasks[team_member] = team_member
        self.notify_observers(task_name,team_member)