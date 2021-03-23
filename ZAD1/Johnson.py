from math import inf

def two_machines_johnson(times:  list):
    tasks = [i for i in range(1, len(times[0])+1)]
    machine1 = [int(i) for i in times[0]]
    machine2 = [int(i) for i in times[1]]
    on_begining = False
    list1, list2 = [], []
    while not tasks == []:
        merged = [*machine1, *machine2]

        min_element = min(merged)
        if min_element in machine1:
            index = machine1.index(min_element)
        else:
            index = machine2.index(min_element)

        if on_begining:
            list1.append(index+1)
            on_begining = False

        else:
            list2.append(index+1)
            on_begining = True

        print(list1, list2)
        machine1[index] = inf
        machine2[index] = inf
        tasks.remove(index+1)

    schedule = list1 + list(list2.__reversed__())
    return schedule

#Naprawic przydzielanie taskow do list

def multi_machines_Johnson(times):
    machine1 = [0 for _ in range(1, len(times[0])+1)]
    machine2 = machine1

    print(times)
    half = int((len(times)) // 2)

    for n in range(0, len(times[0])):
        for i in range(0, half):
            machine1[i] += times[n][i]
        for j in range(half-1, len(times)):
            machine2[j] += times[n][j]

    two_machines_johnson([*machine1, *machine2])
