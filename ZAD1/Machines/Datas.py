import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class Dataset:
    def __init__(self, id, machines, tasks):
        self.id = id
        self.machines = machines
        self.tasks = tasks


def readData(name="data.txt"):
    data_sets = []
    is_reading = True
    with open(os.path.join(THIS_FOLDER, "../data.txt"), "r") as data:
        while is_reading:
            line = data.readline()
            if "data" in line:
                id = int(line.split(sep=".")[1].replace(":", ""))
                line = data.readline().split()
                tasks_amount, machines_amount = int(line[0]), int(line[1])
                tasks_times = []

                for i in range(tasks_amount):
                    tmp = data.readline().split()
                    for k in range(0, len(tmp)):
                        tmp[k] = int(tmp[k])
                    tasks_times.append(tmp)

                data_sets.append(Dataset(id, machines_amount, tasks_times))

            if line == "END":
                is_reading = False

    return data_sets
