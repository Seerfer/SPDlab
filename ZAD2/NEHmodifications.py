import math
import Cmax
import Critical_path

def bigest_Cmax(result, times):
    cmaxs = {}
    if len(result) == 1:
        return result[0]
    else:
        for i in result:
            tmp_result = result[:]
            tmp_result.remove(i)
            tmp_tasks = times[:]
            tmp_tasks.remove(tmp_tasks[i - 1])
            cmaxs[i] = neh_cmax(times, tmp_result)
        return list(dict(sorted(cmaxs.items(), key=lambda item: item[1], reverse=True)).items())[-1][0]


def all_posibilities(lista, el):
    print(lista)
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

        tmp_result = list(range(1, len(result) + 1))
        tmp_task = []
        for i in result:
            tmp_task.append(times[i - 1])
        longest_task = Critical_path.longest_task_ex1(tmp_result, tmp_task)
        longest_task_el = result[longest_task-1]
        result.remove(longest_task_el)
        posibilities = all_posibilities(result, longest_task_el)
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

        tmp_result = list(range(1, len(result) + 1))
        tmp_task = []
        for i in result:
            tmp_task.append(times[i - 1])
        task_with_biggest_sum = Critical_path.task_with_biggest_sum_ex2(tmp_result, tmp_task)
        result.remove(result[task_with_biggest_sum-1])
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

        tmp_result = list(range(1, len(result)+1))
        tmp_task = []
        for i in result:
            tmp_task.append(times[i-1])
        most_operations_task = Critical_path.most_operations_task_ex3(tmp_result, tmp_task)
        result.remove(result[most_operations_task-1])
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
        longest_task = bigest_Cmax(result, times)
        result.remove(longest_task)
        posibilities = all_posibilities(result, longest_task)
        minimum = math.inf
        for i in posibilities:
            c_max = neh_cmax(times, i)
            if c_max < minimum:
                minimum = c_max
                result = i

    return result, minimum

