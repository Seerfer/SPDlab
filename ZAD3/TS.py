import math
from neh import NEHmodifications, Cmax
from Johnson import Johnson
import random
from time import perf_counter
import matplotlib.pyplot as plt

"""
Funkcje potrzebne do generowania listy sąsiedztw i szukania najlepszego elementu z tej listy
"""


def swap_neighbourhoods(schedule, neighbourhoods):
    for i in range(0, len(schedule)):
        temp_schedule = schedule[:]
        for j in range(i + 1, len(schedule)):
            temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]
            if temp_schedule not in neighbourhoods:
                neighbourhoods.append(temp_schedule[:])
            temp_schedule[i], temp_schedule[j] = temp_schedule[j], temp_schedule[i]
    return neighbourhoods


def insert_neighbourhoods(schedule, neighbourhoods):
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


def inverse_neighbourhoods(schedule, neighbourhoods, inverse_len):
    for i in range(0, len(schedule) - inverse_len + 1):
        tmp1 = schedule[:]
        tmp2 = schedule[i:i + inverse_len]
        tmp2.reverse()
        for k in range(inverse_len):
            tmp1[i + k] = tmp2[k]
        if tmp1 not in neighbourhoods:
            neighbourhoods.append(tmp1)
    return neighbourhoods

def neighbourhoods_generator(schedule, function="swap", inverse_len=4):
    neighbourhoods_list = []
    functions = function.split(",")
    if "swap" in functions:
        neighbourhoods_list.extend(swap_neighbourhoods(schedule, neighbourhoods=neighbourhoods_list[:]))

    if "insert" in functions:
        neighbourhoods_list.extend(insert_neighbourhoods(schedule, neighbourhoods=neighbourhoods_list[:]))

    if "inverse" in functions:
        neighbourhoods_list.extend(inverse_neighbourhoods(schedule, neighbourhoods=neighbourhoods_list[:], inverse_len=inverse_len))
    return neighbourhoods_list


def best_neighbourhood(schedules, times, tabu, current):
    cmin = Cmax.count_cmax(current, list((map(list, zip(*times)))))
    change = False
    tmp = schedules[0]
    for schedule in schedules:
        if schedule not in tabu:
            cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
            if cmax < cmin:
                cmin = cmax
                tmp = schedule
                change = True
    if not change:
        for schedule in tabu:
            cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
            if cmax < cmin:
                cmin = cmax
                tmp = schedule

    return cmin, tmp

def global_neighbourhoods(current, zones=40, zone_scale=97):
    tmp = []
    tmp_neigh = neighbourhoods_generator(current, function="inverse",
                                                  inverse_len=len(current)-zones)
    for neigh in tmp_neigh:
        print(neigh)
        tmp.extend(neighbourhoods_generator(neigh, function="inverse",
                                                    inverse_len=len(current)-zone_scale))
    return tmp
"""
Funkcje do realizacji algorytmu tabu search
"""


def initialize_shedule(times, method="random"):
    if method == "algorithm":
        if len(times) < 101:
            return NEHmodifications.neh_ext4(times)[0]
        else:
            return Johnson.multi_machines_Johnson(times)
    if method == "random":
        tmp = list(range(1, len(times)+1))
        random.shuffle(tmp)
        return tmp
    if method == "sequence":
        return list(range(1, len(times)+1))


def make_search(times, tabu, max_tabu, current, best_cmax, best, change, history):
    if change:
        neighbourhoods = neighbourhoods_generator(current,function="swap")
    else:
        neighbourhoods = global_neighbourhoods(current)
        neighbourhoods.extend(neighbourhoods_generator(current,function="insert"))
    current_cmax, current = best_neighbourhood(neighbourhoods, times, tabu, current)
    history.append(current_cmax)
    print(f"best: {best_cmax}            current: {current_cmax}")
    tabu.append(current)
    if len(tabu) > max_tabu:
        tabu.pop(0)
    if current_cmax < best_cmax:
        best = current
        best_cmax = current_cmax
        change = True
    else:
        change = False

    return best, best_cmax, tabu, current, change


def Tabu_search(times, stop="stuck", max_tabu=25, iter=200, stop_time=100,  stuck_point=10):
    history = []
    schedule = initialize_shedule(times)
    best = schedule
    best_cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
    tabu = [schedule]
    current = schedule[:]

    if stop == "iter":
        for i in range(0, iter):
            tmp = make_search(times, tabu, max_tabu, current, best_cmax, best)
            best = tmp[0]
            best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]


    if stop == "times":
        start = perf_counter()
        end = 0
        while end-start < stop_time:
            tmp = make_search(times, tabu, max_tabu, current, best_cmax, best, history)
            best = tmp[0]
            best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]
            end = perf_counter()

    if stop == "stuck":
        i = 0
        change = False
        break_point = True
        while break_point:
            tmp = make_search(times, tabu, max_tabu, current, best_cmax, best, change, history)
            if tmp[0] != best:
                i = 0
            else:
                i += 1
            best = tmp[0]
            best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]
            change = tmp[4]
            if i == stuck_point:
                break_point = False

    plt.plot(list(range(len(history))), history)
    plt.show()
    return best, best_cmax
