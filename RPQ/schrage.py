from Task import Task
from typing import List
from Heapq import Heapq
import sys

def schrage(tasks: List[Task]):
    order = []
    C = []
    ready = set()
    Cmax = 0
    not_ready = set(tasks)
    t = min(task.get_r() for task in not_ready)
    while ready or not_ready:
        while not_ready and min(task.get_r() for task in not_ready) <= t:
            e = min(not_ready, key=Task.get_r)
            ready.add(e)
            not_ready.remove(e)

        if not ready:
            t = min(task.get_r() for task in not_ready)
        else:
            e = max(ready, key=Task.get_q)
            ready.remove(e)
            order.append(e)
            t += e.get_p()
            C.append(t)
            Cmax = max(Cmax, t + e.q)

    return order, Cmax, C


def schrage_heapq(tasks: List[Task]):
    order = []
    C = []
    ready = Heapq(key="q", reverse=True)
    Cmax = 0
    not_ready = Heapq(tasks=tasks, key="r", reverse=False)
    t = not_ready.top.r
    while ready or not_ready:
        while not_ready and not_ready.top.r <= t:
            ready.insert(not_ready.pop())
        if not ready:
            t = not_ready.top.r
        else:
            e = ready.top
            ready.pop()
            order.append(e)
            t += e.p
            C.append(t)
            Cmax = max(Cmax, t + e.q)

    return order, Cmax, C

def schrage_pmtn(tasks: List[Task]):
    ready = set()
    Cmax = 0
    not_ready = set(tasks)
    l = Task(0, 0, sys.maxsize, -1)
    t = min(task.get_r() for task in not_ready)
    while ready or not_ready:
        while not_ready and min(task.get_r() for task in not_ready) <= t:
            e = min(not_ready, key=Task.get_r)
            ready.add(e)
            not_ready.remove(e)
            if e.get_q() > l.get_q():
                l = l.copy().change_p(t - e.get_r()) ##tutaj byla zmiana na z kopia
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
                l = l.copy().change_p(t - e.get_r())
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
