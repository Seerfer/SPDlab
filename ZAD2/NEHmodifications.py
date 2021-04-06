import math
import Cmax

def all_posibilities(lista, el):
    posibilities = []
    i = 0
    for _ in range(len(lista)+1):
        tmp = lista[:]
        tmp.insert(i, el)
        i = i+1
        posibilities.append(tmp)
    return posibilities


def neh_cmax(tasks, schedule):
    tmp_schedule = list(range(1, len(schedule)+1))
    tmp_tasks =  []
    for i in schedule:
        tmp_tasks.append(tasks[i-1])
    return Cmax.count_cmax(tmp_schedule, list((map(list, zip(*tmp_tasks)))))


def neh_ext4(times):
    priorities_dict = {}
    index = 1

    for i in times:
        priorities_dict[index] = sum(i)
        index += 1
    priorities_dict = dict(sorted(priorities_dict.items(), key=lambda item: item[1], reverse=True))

    result = []
    while list(priorities_dict.values()):
        choose = list(priorities_dict.keys())[0]
        priorities_dict.pop(choose)
        if len(result) == 0:
            result.append(choose)

        else:
            posibilities = all_posibilities(result, choose)
            minimum = math.inf
            for i in posibilities:
                c_max = neh_cmax(times, i)
                if c_max < minimum:
                    minimum = c_max
                    result = i

    # ROZSZERZENIE #
    cmaxs = {}
    for i in result:
        tmp_result = result[:]
        tmp_result.remove(i)
        tmp_tasks = times[:]
        tmp_tasks.remove(tmp_tasks[i-1])
        cmaxs[i] = neh_cmax(times, tmp_result)
    longest_task = list(dict(sorted(cmaxs.items(), key=lambda item: item[1], reverse=True)).items())[-1][0] #  Numer zadania
    result.remove(longest_task)
    posibilities = all_posibilities(result, longest_task)
    minimum = math.inf
    for i in posibilities:
        c_max = neh_cmax(times, i)
        if c_max < minimum:
            minimum = c_max
            result = i

    return result, minimum
