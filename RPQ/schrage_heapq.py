from Task import Task
from typing import List
from Heapq import Heapq

def schrage_heap(tasks: List[Task]) -> List[Task]:
    order = []
    ready = Heapq(key="q", reverse=True)
    Cmax = 0
    not_ready = Heapq(tasks=tasks, key="r", reverse=False)
    t = not_ready.top.r
    while ready or not_ready:
        while not_ready and not_ready.top.r <= t:
            e = not_ready.pop()
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