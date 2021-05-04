from Task import Task
from typing import List
from Heapq import Heapq

def schrage(tasks: List[Task]) -> List[Task]:
    order = []
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
            order.append(e.id)
            t += e.get_p()
            Cmax = max(Cmax, t+e.q)

    return order, Cmax

def schrage_heapq(tasks: List[Task]) -> List[Task]:
    order = []
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
            order.append(e.id)
            t += e.p
            Cmax = max(Cmax, t+e.q)

    return order, Cmax