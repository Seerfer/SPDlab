from Task import Task
from typing import List
import sys

def schrage_pmtn(tasks: List[Task]) -> List[Task]:
    ready = set()
    Cmax = 0
    not_ready = set(tasks)
    l = Task(0, 0, sys.maxsize, 0)
    t = min(task.get_r() for task in not_ready)
    while ready or not_ready:
        while not_ready and min(task.get_r() for task in not_ready) <= t:
            e = min(not_ready, key=Task.get_r)
            ready.add(e)
            not_ready.remove(e)
            if e.get_q() > l.get_q():
                l.p = t - e.r
                t = e.r
                if l.p > 0:
                    ready.add(l)

        if not ready:
            t = min(task.get_r() for task in not_ready)
        else:
            e = max(ready, key=Task.get_q)
            ready.remove(e)
            l = e
            t += e.p
            Cmax=max(Cmax,t+e.q)
    return Cmax
