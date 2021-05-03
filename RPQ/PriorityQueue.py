from Task import Task

class PriorityQueue:
    def __init__(self, tasks:list, key):
        if key == "q":
            self.queue = sorted(tasks, key=lambda task: task.q)
        elif key == "r":
            self.queue = sorted(tasks, key=lambda task: task.r)
        else:
            self.queue = tasks

    def pop(self):
        return self.queue.pop(0)

    @property
    def size(self):
        return len(self.queue)

    @property
    def isEmpty(self):
        return (len(self.queue) == 0)