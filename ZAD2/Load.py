import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def readData(name):
    matrix = []
    with open(os.path.join(THIS_FOLDER, name), "r") as data:
        line = data.readline().split()
        tasks,  machines = int(line[0]), int(line[1])
        for _ in range(0, tasks):
            matrix.append([int(x) for x in next(data).split()])

        return matrix
