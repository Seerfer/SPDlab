import os
from Task import Task

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def readData(name):
    tasks = []
    with open(os.path.join(THIS_FOLDER, name), "r") as data:
        line = int(data.readline())
        for id in range(line):
            r, p, q = data.readline().split()
            tasks.append(Task(r, p, q, id+1))
        return tasks
