import math
from itertools import permutations
import C_max


def total_review(times):
    tasks = len(times[0])
    schedules = list(permutations(range(1,(tasks+1))))
    Cmax = math.inf
    best_schedule = 0
    for i in range(0,len(schedules)):
        Cmax_= C_max.calculate_Cmax(schedules[i], times)
        if Cmax_ < Cmax:
            Cmax = Cmax_
            best_schedule = i
    return schedules[best_schedule],Cmax
