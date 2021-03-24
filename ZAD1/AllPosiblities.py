import math
from itertools import permutations
import Cmax


def all_posibilities(times):
    schedules = list(permutations(range(1, (len(times[0]) + 1))))
    cmax, best = math.inf, 0
    for i in range(0, len(schedules)):
        cmax_ = Cmax.calculate_cmax(schedules[i], times)
        if cmax_ < cmax:
            cmax = cmax_
            best = i
    return schedules[best], cmax
