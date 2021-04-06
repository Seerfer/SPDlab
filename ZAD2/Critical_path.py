def critical_path(sched, times):
    times = list((map(list, zip(*times))))
    crit_path = []
    crit_time = 0
    tmp = [[None for _ in range(len(times[0]))] for _ in range(len(times))]
    for i in range(0, len(times)):
        for j in range(len(times[0])):
            if i == 0:
                if j == 0:
                    tmp[i][j] = times[sched[i] - 1][j]
                    crit_path.append((sched[i], j+1))
                    crit_time += times[sched[i] - 1][j]
                else:
                    tmp[i][j] = (tmp[i][j - 1] + times[sched[i] - 1][j])
            else:
                if j == 0:
                    tmp[i][j] = tmp[i - 1][j] + times[sched[i] - 1][j]
                else:
                    tmp[i][j] = max(tmp[i - 1][j], tmp[i][j - 1]) + times[sched[i] - 1][j]
                    if (tmp[i][j-1]) >= (tmp[i-1][j]):
                        if ((tmp[i][j-1]) - (times[sched[i]-1][j-1])) == crit_time:
                            crit_path.append((sched[i], j))
                            crit_time += times[sched[i] - 1][j-1]
                    else:
                        if ((tmp[i-1][j]) - (times[sched[i-1]-1][j])) == crit_time:
                            crit_path.append((sched[i-1], j+1))
                            crit_time += times[sched[i] - 1][j]
                    if i == len(times)-1:
                        if j == len(times[0])-1:
                            if ((tmp[i][j]) - (times[i][j])) == crit_time:
                                crit_path.append((sched[i], j+1))
                                crit_time += times[i][j]
    return crit_path


def longest_task_ex1(sched, times):
    crit_path = critical_path(sched, times)
    times = list((map(list, zip(*times))))
    max_time = 0
    task_with_max = 0
    for item in crit_path:
        task, machine = item
        time = times[task-1][machine-1]
        if time > max_time:
            max_time = time
            task_with_max = task
    return task_with_max


def task_with_biggest_sum_ex2(sched, times):
    crit_path = critical_path(sched, times)
    times = list((map(list, zip(*times))))
    biggest_sum_task = None
    sum = {}
    for item in crit_path:
        task, machine = item
        time = times[task - 1][machine - 1]
        if task in sum:
            sum[task] += time
        else:
            sum[task] = time
    if sum:
        biggest_sum_task = max(sum, key=sum.get)
    return biggest_sum_task


def most_operations_task_ex3(sched, times):
    crit_path = critical_path(sched, times)
    tasks = []
    task_most = 0
    most = 0
    for item in crit_path:
        task, machine = item
        tasks.append(task)
    for item in tasks:
        operations = tasks.count(item)
        if operations > most:
            most = operations
            task_most = item
    return task_most
