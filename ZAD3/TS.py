import math
from neh import NEHmodifications, Cmax
from Johnson import Johnson
import random
from time import perf_counter
def initialize_shedule(times, method="neh"):
    if method == "neh":
        if len(times) < 101:
            return NEHmodifications.neh_ext4(times)[0]
        else:
            return Johnson.multi_machines_Johnson(times)
    if method == "random":
        return random.shuffle(list(range(1, len(times)+1)))
    if method == "sequence":
        return list(range(1, len(times)+1))

def neighbours(schedule, neighbours_number="all", function="swap", inverse_numbers=None):
    neighbours = []
    functions = function.split(",")
    if str(neighbours_number) == "all":
        if "swap" in functions:
            for i in range(0, len(schedule)):
                temp_schedule = schedule[:]
                for j in range(i + 1, len(schedule)):
                    temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]
                    neighbours.append(temp_schedule[:])
                    temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]

            return neighbours
        if "insert" in functions:
            for i in range(0, len(schedule)):
                temp_schedule = schedule[:]
                current = temp_schedule.pop(i)
                for j in range(0, len(schedule)):
                    if j != i:
                        temp_schedule.insert(j, current)
                        if temp_schedule not in neighbours:
                            neighbours.append(temp_schedule[:])
                        temp_schedule.pop(j)

            return neighbours
        if "inverse" in functions:
            pass

    else:
        counter = 0
        if "swap" in functions:
            for i in range(0, int(neighbours_number)):
                temp_schedule = schedule[:]
                for j in range(i + 1, len(schedule)):
                    temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]
                    neighbours.append(temp_schedule[:])
                    temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]

            return neighbours
        if "insert" in functions:
            for i in range(0, len(schedule)):
                temp_schedule = schedule[:]
                current = temp_schedule.pop(i)
                for j in range(0, len(schedule)):
                    if j != i:
                        temp_schedule.insert(j, current)
                        if temp_schedule not in neighbours:
                            neighbours.append(temp_schedule[:])
                        temp_schedule.pop(j)

            return neighbours
        if "inverse" in functions:
            pass

def best_neighbour(schedules, times):
    cmin = math.inf
    tmp = None
    for schedule in schedules:
        cmax = Cmax.count_cmax(schedule,times)
        if cmax < cmin:
            cmin = cmax
            tmp = schedule
    return tmp

def Tabu_search(times, naighbours, stop="iter", iter=5000, stop_time=1000000):
    schedule = initialize_shedule(times)
    best = schedule
    tabu = []
    tabu.append(schedule)

    if stop == "iter":
        for i in range(0, iter):
            neighbourhoods = neighbours(times, schedule)
            best_cmax = math.inf
            best_current = neighbours[0]
            for i in range(1, len(neighbourhoods)):
                pass



    if stop == "times":
        start = perf_counter()
        end = math.inf
        while end-start > stop_time:



            end = perf_counter()
