from data_objects.task_info import TaskInfo


class TaskGraph:
    def __init__(self):
        self.graph:list[TaskInfo] = []

    def add_task(self, task_info:TaskInfo):
        self.graph.append(task_info)

    def add_tasks(self, tasks_info:list[TaskInfo]):
        [self.add_task(task_info) for task_info in tasks_info]

    def get_task_graph(self):
        return self.graph