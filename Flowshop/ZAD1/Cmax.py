def count_cmax(sched, times):
    times = list((map(list, zip(*times))))
    tmp = [[None for _ in range(len(times[0]))] for _ in range(len(times))]
    for i in range(0, len(times)):
        for j in range(len(times[0])):
            if i == 0:
                if j == 0:
                    tmp[i][j] = times[sched[i] - 1][j]
                else:
                    tmp[i][j] = (tmp[i][j - 1] + times[sched[i] - 1][j])
            else:
                if j == 0:
                    tmp[i][j] = tmp[i - 1][j] + times[sched[i] - 1][j]
                else:
                    tmp[i][j] = max(tmp[i - 1][j], tmp[i][j - 1]) + times[sched[i] - 1][j]

    return tmp[len(times) - 1][len(times[0]) - 1]
