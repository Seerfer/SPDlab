from neh import NEHmodifications, Cmax
from ZAD3 import Johnson
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
    if method == "neh":
        return NEHmodifications.neh_ext4(times)[0]
    if method == "johnson":
        return Johnson.multi_machines_Johnson(times)
    if method == "random":
        tmp = list(range(1, len(times)+1))
        random.shuffle(tmp)
        return tmp
    if method == "sequence":
        return list(range(1, len(times)+1))


def make_search(times, tabu, max_tabu, current, best_cmax, best, history):
    neighbourhoods = neighbourhoods_generator(current,function="swap")
    tmp_tabu = tabu[-max_tabu:]
    current_cmax, current = best_neighbourhood(neighbourhoods, times, tmp_tabu[:], current)
    history.append(current_cmax)
    print(f"best: {best_cmax}            current: {current_cmax}")
    tabu.append(current)
    if current_cmax < best_cmax:
        best = current
        best_cmax = current_cmax

    return best, best_cmax, tabu, current,


def Tabu_search(times, stop="stuck", max_tabu=20, iter=80, stop_time=100,  stuck_point=20):
    global i, global_cmax
    history = []
    init_tabu = max_tabu
    schedule = initialize_shedule(times, method="johnson")
    best = schedule
    best_cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
    tabu = [schedule]
    current = schedule[:]

    if stop == "iter":
        for i in range(0, iter):
            tmp = make_search(times, tabu[:], max_tabu, current, best_cmax, best, history)
            best = tmp[0]
            if best_cmax == tmp[1]:
                max_tabu -= 1
            else:
                max_tabu = init_tabu
                best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]


    if stop == "times":
        start = perf_counter()
        end = 0
        after_reset = True
        while end-start < stop_time:
            tmp = make_search(times, tabu, max_tabu, current, best_cmax, best, history)
            if tmp[0] != best:
                i = 0
            else:
                i += 1
            best = tmp[0]
            if best_cmax == tmp[1]:
                max_tabu -= 1
            best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]

            if i == 10:
                print("reset")
                global_cmax = best_cmax
                after_reset = True
                i = 0
                current = initialize_shedule(times, method="random")
                tabu = [current]
                best_cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
                best = current

            if after_reset:
                if best_cmax < global_cmax:
                    global_cmax = best_cmax
            end = perf_counter()


    if stop == "stuck":
        i = 0
        break_point = True
        while break_point:
            tmp = make_search(times, tabu[:], max_tabu, current, best_cmax, best, history)
            if tmp[0] != best:
                i = 0
            else:
                i += 1
            best = tmp[0]
            if best_cmax == tmp[1]:
                max_tabu -= 1
            else:
                max_tabu = init_tabu
                best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]
            if i == stuck_point:
                break_point = False

    if stop == "forever":
        i = 0
        after_reset = False
        while True:
            tmp = make_search(times, tabu, max_tabu, current, best_cmax, best, history)
            if tmp[0] != best:
                i = 0
            else:
                i += 1
            best = tmp[0]
            if best_cmax == tmp[1]:
                max_tabu -= 1
            best_cmax = tmp[1]
            tabu = tmp[2]
            current = tmp[3]

            if i == 10:
                print("reset")
                global_cmax = best_cmax
                after_reset = True
                i = 0
                current = initialize_shedule(times, method="random")
                tabu = [current]
                best_cmax = Cmax.count_cmax(schedule, list((map(list, zip(*times)))))
                best = current

            if after_reset:
                if best_cmax < global_cmax:
                    global_cmax = best_cmax
                    global_best = best
                    file = open("best.txt", "w")
                    file.write(f"{global_cmax} : {global_best}")
                    file.close()
            else:
                file = open("best.txt", "w")
                file.write(f"{best_cmax} : {best}")
                file.close()

    #plt.plot(list(range(len(history))), history)
    #plt.show()
    return best, best_cmax, history
