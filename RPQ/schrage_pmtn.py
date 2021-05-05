from Task import Task
from typing import List
import sys
from Heapq import Heapq


def schrage_pmtn(tasks: List[Task]):
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
            if e.q > l.q:
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
            Cmax = max(Cmax, t + e.q)
    return Cmax


def schrage_pmtn_heapq(tasks: List[Task]):
    ready = Heapq(key="q", reverse=True)
    Cmax = 0
    l = Task(0, 0, sys.maxsize, 0)
    not_ready = Heapq(tasks=tasks, key="r", reverse=False)
    t = not_ready.top.r
    while ready or not_ready:
        while not_ready and not_ready.top.r <= t:
            e = not_ready.pop()
            ready.insert(e)
            if e.q > l.q:
                l.p = t - e.r
                t = e.r
                if l.p > 0:
                    ready.insert(l)
        if not ready:
            t = not_ready.top.r
        else:
            e = ready.pop()
            l = e
            t += e.p
            Cmax = max(Cmax, t + e.q)

    return Cmax
