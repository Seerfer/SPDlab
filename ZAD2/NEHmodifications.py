import math
import Cmax
import Critical_path
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


def neh_ext1(times):
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
    longest_task = Critical_path.longest_task_ex1(result, times)
    result.remove(longest_task)
    posibilities = all_posibilities(result, longest_task)
    minimum = math.inf
    for i in posibilities:
        c_max = neh_cmax(times, i)
        if c_max < minimum:
            minimum = c_max
            result = i

    return result, minimum

def neh_ext2(times):
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
    task_with_biggest_sum = Critical_path.task_with_biggest_sum_ex2(result, times)
    result.remove(task_with_biggest_sum)
    posibilities = all_posibilities(result, task_with_biggest_sum)
    minimum = math.inf
    for i in posibilities:
        c_max = neh_cmax(times, i)
        if c_max < minimum:
            minimum = c_max
            result = i

    return result, minimum


def neh_ext3(times):
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
    most_operations_task = Critical_path.most_operations_task_ex3(result, times)
    result.remove(most_operations_task)
    posibilities = all_posibilities(result, most_operations_task)
    minimum = math.inf
    for i in posibilities:
        c_max = neh_cmax(times, i)
        if c_max < minimum:
            minimum = c_max
            result = i

    return result, minimum


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

