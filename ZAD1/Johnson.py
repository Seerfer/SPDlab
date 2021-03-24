from math import inf


def two_machines_johnson(times: list):
    tasks = [i for i in range(1, len(times[0]) + 1)]
    machine1 = [int(i) for i in times[0]]
    machine2 = [int(i) for i in times[1]]
    list1, list2 = [], []

    while True:
        merged = [*machine1, *machine2]

        min_element = min(merged)
        if min_element in machine1:
            index = machine1.index(min_element)
            list1.append(index + 1)
        else:
            index = machine2.index(min_element)
            list2.append(index + 1)

        machine1[index] = inf
        machine2[index] = inf
        tasks.remove(index + 1)

        if not tasks:
            break

    list2 = list(reversed(list2))
    schedule = list1 + list2
    return schedule


def multi_machines_Johnson(times):
    if len(times) % 2 == 0:
        half = len(times) // 2
        list1 = times[:half]
        list2 = times[half:]
        list1 = [sum(i) for i in zip(*list1)]
        list2 = [sum(i) for i in zip(*list2)]

    else:
        half = len(times) // 2
        half_element = times[half]
        list1 = times[0:half]
        list2 = times[half + 1:]

        list1 = [sum(i) for i in zip(*list1)]
        list2 = [sum(i) for i in zip(*list2)]

        list1 = [a + b for a, b in zip(list1, half_element)]
        list2 = [a + b for a, b in zip(list2, half_element)]

    splited_lists = [list1, list2]
    return two_machines_johnson(splited_lists)
