class Task:
    def __init__(self, id, time):
        self.id = id
        self.time = time



class Machine:
    def __init__(self, id):
        self.id = id
        self.tasks_todo = []

    def add_task(selfs, task):
        selfs.tasks_todo.append(task)

    def show_tasks(self):
        for task in self.tasks_todo:
            print(f"Task id: {task.id}, task time: {task.time}")
