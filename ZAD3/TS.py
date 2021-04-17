import math
from neh import NEHmodifications, Cmax
from Johnson import Johnson
import random
from time import perf_counter


"""
Funkcje potrzebne do generowania listy sąsiedztw i szukania najlepszego elementu z tej listy
"""


def swap_neighbourhoods(schedule):
    neighbourhoods = []
    for i in range(0, len(schedule)):
        temp_schedule = schedule[:]
        for j in range(i + 1, len(schedule)):
            temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]
            neighbourhoods.append(temp_schedule[:])
            temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]
    return neighbourhoods


def insert_neighbourhoods(schedule):
    neighbourhoods = []
    for i in range(0, len(schedule)):
        temp_schedule = schedule[:]
        current = temp_schedule.pop(i)
        for j in range(0, len(schedule)):
            if j != i:
                temp_schedule.insert(j, current)
                if temp_schedule not in neighbourhoods:
                    neighbourhoods.append(temp_schedule[:])
                temp_schedule.pop(j)
    return neighbourhoods


def inverse_neighbourhoods(schedule, inverse_len):
    neighbourhoods = []
    for i in range(0, len(schedule) - inverse_len + 1):
        tmp1 = schedule[:]
        tmp2 = schedule[i:i + inverse_len]
        tmp2.reverse()
        for k in range(inverse_len):
            tmp1[i + k] = tmp2[k]
        neighbourhoods.append(tmp1)
    return neighbourhoods

def neighbourhoods_generator(schedule, neighbourhoods_number="all", function="swap", inverse_len=3):
    neighbourhoods = []
    functions = function.split(",")

    if "swap" in functions:
        neighbourhoods.extend(swap_neighbourhoods(schedule))

    if "insert" in functions:
        neighbourhoods.extend(insert_neighbourhoods(schedule))

    if "inverse" in functions:
        neighbourhoods.extend(inverse_neighbourhoods(schedule, inverse_len))

    return neighbourhoods


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



"""
Funkcje do realizacji algorytmu tabu search
"""


def initialize_shedule(times, method="algorithm"):
    if method == "algorithm":
        if len(times) < 101:
            return NEHmodifications.neh_ext4(times)[0]
        else:
            return Johnson.multi_machines_Johnson(times)
    if method == "random":
        return random.shuffle(list(range(1, len(times)+1)))
    if method == "sequence":
        return list(range(1, len(times)+1))


def Tabu_search(times, stop="stuck", max_tabu=8, iter=1000, stop_time=100,  stuck_point=20):
    schedule = initialize_shedule(times)
    best = schedule
    best_cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
    tabu = [schedule]
    current = schedule[:]

    if stop == "iter":
        for i in range(0, iter):
            neighbourhoods = neighbourhoods_generator(current, times, function="swap")
            current_cmax, current = best_neighbour(neighbourhoods, times, tabu)
            tabu.append(current)
            if len(tabu) > max_tabu:
                tabu.pop(0)
            if current_cmax < best_cmax:
                best = current
                best_cmax = current_cmax


    if stop == "times":
        start = perf_counter()
        end = 0
        while end-start < stop_time:
            neighbourhoods = neighbourhoods_generator(current, times, function="swap")
            current_cmax, current = best_neighbour(neighbourhoods, times, tabu)
            tabu.append(current)
            if len(tabu) > max_tabu:
                tabu.pop(0)
            if current_cmax < best_cmax:
                best = current
                best_cmax = current_cmax
            end = perf_counter()


    if stop == "stuck":
        i = 0
        break_point = True
        while break_point:
            neighbourhoods = neighbourhoods_generator(current, times, function="swap")
            current_cmax, current = best_neighbour(neighbourhoods, times, tabu)
            tabu.append(current)
            if len(tabu) > max_tabu:
                tabu.pop(0)
            i += 1
            if current_cmax < best_cmax:
                best = current
                best_cmax = current_cmax
                i = 0
            if i > stuck_point:
                break_point = False

    return best, best_cmax