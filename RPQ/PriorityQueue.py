from Task import Task

class PriorityQueue:
    def __init__(self, tasks, key):
        self.queue = []

        if key == "q":
            pass
        if key == "r":
            pass
        else:
            raise RuntimeError("Wrong key")

    @property
    def size(self):
        return len(self.queue)

    @property
    def isEmpty(self):
        return (len(self.queue) == 0)