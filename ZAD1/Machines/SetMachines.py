from Machines.Datas import readData
from Machines.Machine import Machine, Task

def load_data(data_set_index, dataset = readData()):
    machines = []
    for i in range(1, dataset[data_set_index].machines + 1):
        machines.append(Machine(i))

    tasks = dataset[data_set_index].tasks
    id = 1

    for task in tasks:
        for i in range(3):
            machines[i].add_task(Task(id, task[i]))
        id += 1

    return machines