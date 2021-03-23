import numpy


def calculate_Cmax(schedule, times):
    times = numpy.transpose(times)
    tasks = len(times)
    machines = len(times[0])
    Cmax = [[0 for x in range(machines)] for y in range(tasks)]
    for i in range(0, tasks):
        for j in range(0, machines):
            if i == 0:
                if j == 0:
                    Cmax[i][j] = times[schedule[i] - 1][j]
                else:
                    Cmax[i][j] = (Cmax[i][j - 1] + times[schedule[i] - 1][j])
            else:
                if j == 0:
                    Cmax[i][j] = Cmax[i - 1][j] + times[schedule[i] - 1][j]
                else:
                    Cmax[i][j] = max(Cmax[i - 1][j], Cmax[i][j - 1]) + times[schedule[i] - 1][j]

    return Cmax[tasks - 1][machines - 1]


