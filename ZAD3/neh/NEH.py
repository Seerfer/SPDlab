import math
from neh.Cmax import count_cmax

def all_posibilities(lista, el):
    posibilities = []
    i = 0
    for _ in range(len(lista)+1):
        tmp = lista[:]
        tmp.insert(i, el)
        i = i+1
        posibilities.append(tmp)
    return posibilities

def neh_cmax(times, schedule):
    tmp_schedule = list(range(1, len(schedule)+1))
    tmp_tasks =  []
    for i in schedule:
        tmp_tasks.append(times[i - 1])
    return count_cmax(tmp_schedule, list((map(list, zip(*tmp_tasks)))))

def neh(times):
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

    return result, minimum