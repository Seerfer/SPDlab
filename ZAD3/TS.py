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

def neighbourhoods_generator(schedule, neighbours_number="all", function="inverse", inverse_len=3):
    neighbours = []
    functions = function.split(",")
    counter = 0
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
        for i in range(0, len(schedule)-inverse_len-1):
            tmp1 = schedule[:]
            tmp2 = schedule[i:i+inverse_len]
            tmp2.reverse()
            for k in range(inverse_len):
                tmp1[i+k] = tmp2[k]
            neighbours.append(tmp1)
        return neighbours

def best_neighbour(schedules, times, tabu):
    cmin = math.inf
    tmp = schedules[0]
    for schedule in schedules:
        if schedule not in tabu:
            cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
            if cmax < cmin:
                cmin = cmax
                tmp = schedule
    return cmin, tmp


def make_tabu_search(times, tabu, current, best_cmax):
    neighbourhoods = neighbourhoods_generator(current, times, function="swap")
    current_cmax, current = best_neighbour(neighbourhoods, times, tabu)
    tabu.append(current)
    if current_cmax < best_cmax:
        best = current
        best_cmax = current_cmax
    return best, best_cmax, current, current_cmax, tabu


def Tabu_search(times, stop="iter", iter=1000, stop_time=100,  stuck_point=20, tabu_size=20, tabu_currents=True):


    schedule = initialize_shedule(times)
    best = schedule
    best_cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
    tabu = []
    tabu.append(schedule)
    current = schedule[:]

    if stop == "iter":
        for i in range(0, iter):
            print(i)
            best, best_cmax, current, current_cmax, tabu = make_tabu_search(times, tabu, current, best_cmax)


    if stop == "times":
        start = perf_counter()
        end = 0
        while end-start < stop_time:
            neighbourhoods = neighbourhoods_generator(current, times, function="swap")
            current_cmax, current = best_neighbour(neighbourhoods, times, tabu)
            tabu.append(current)
            if current_cmax < best_cmax:
                best = current
                best_cmax = current_cmax
            end = perf_counter()
            print(end - start)


    if stop == "stuck":
        i = 0
        break_point = True
        while break_point:
            neighbourhoods = neighbourhoods_generator(current, times, function="swap")
            current_cmax, current = best_neighbour(neighbourhoods, times, tabu)
            tabu.append(current)
            i += 1
            if current_cmax < best_cmax:
                best = current
                best_cmax = current_cmax
                i = 0
            if i > stuck_point:
                break_point = False

    return best, best_cmax