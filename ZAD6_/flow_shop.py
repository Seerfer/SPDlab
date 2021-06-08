from ortools.sat.python import cp_model
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def readData(name):
    matrix = []
    with open(os.path.join(THIS_FOLDER, name), "r") as data:
        line = data.readline().split()
        tasks,  machines = int(line[0]), int(line[1])
        for _ in range(0, tasks):
            matrix.append([int(x) for x in next(data).split()])

        return matrix,tasks,machines

def read_datest(name):
    data_sets = []
    is_reading = True
    with open(os.path.join(THIS_FOLDER, name), "r") as data:
        while is_reading:
            line = data.readline()
            if "data" in line:
                line = data.readline().split()
                tasks_amount, machines_amount = int(line[0]), int(line[1])

                matrix = []

                for _ in range(0, tasks_amount):
                    matrix.append([int(x) for x in next(data).split()])

                data.readline()
                data.readline()
                cmax = int(data.readline())
                result = [int(x) for x in next(data).split()]
                data_sets.append(matrix)

            if line == "END":
                is_reading = False

    return data_sets

def solve_flow_shop_with_ortools(filename):
    data,tasks,machines = readData(filename)
    model = cp_model.CpModel()
    task_type = collections.namedtuple('task_type', 'start end interval')
