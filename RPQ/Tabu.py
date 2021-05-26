import random
import math
import Cmax
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


def neighbourhoods_generator(schedule, function="swap", inverse_len=3):
    neighbourhoods_list = []
    functions = function.split(",")
    if "swap" in functions:
        neighbourhoods_list = swap_neighbourhoods(schedule, neighbourhoods=neighbourhoods_list)
    if "insert" in functions:
        neighbourhoods_list = insert_neighbourhoods(schedule, neighbourhoods=neighbourhoods_list)
    if "inverse" in functions:
        neighbourhoods_list = inverse_neighbourhoods(schedule, neighbourhoods=neighbourhoods_list, inverse_len=inverse_len)
    return neighbourhoods_list


def best_neighbourhood(schedules, tasks, tabu):
    cmin = math.inf
    tmp = schedules[0]
    for schedule in schedules:
        if schedule not in tabu:
            cmax = Cmax.cmax(tasks, schedule)
            if cmax < cmin:
                cmin = cmax
                tmp = schedule
    if cmin == math.inf:
        for schedule in tabu:
            cmax = Cmax.cmax(tasks, schedule)
            if cmax < cmin:
                cmin = cmax
                tmp = schedule

    return cmin, tmp

"""
Funkcja do generowania rozwiązania początkowego
"""
def initialize_schedule(times):
    tmp = list(range(1, len(times) + 1))
    random.shuffle(tmp)
    return tmp


def make_search(times, tabu, max_tabu, current, best_cmax, best, history, method):
    neighbourhoods = neighbourhoods_generator(current, function=method)
    tmp_tabu = tabu[-max_tabu:]
    current_cmax, current = best_neighbourhood(neighbourhoods, times, tmp_tabu[:])
    history.append(current_cmax)
    print(f"best: {best_cmax}            current: {current_cmax}")
    tabu.append(current)
    if current_cmax < best_cmax:
        best = current
        best_cmax = current_cmax
    return best, best_cmax, tabu, current


def Tabu_search(tasks, max_tabu=30, iter=100,
                neighbourhoods_function="swap"):
    history = []
    schedule = initialize_schedule(tasks)
    best = schedule
    best_cmax = Cmax.cmax(tasks, schedule)
    tabu = [schedule]
    current = schedule[:]

    for _ in range(3):
        for _ in range(iter):
            tmp = make_search(tasks, tabu[:], max_tabu, current, best_cmax, best, history, neighbourhoods_function)
            best = tmp[0]
            best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]
        print("restart")
        current=initialize_schedule(tasks)
    return best_cmax