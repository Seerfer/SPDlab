from Task import Task
from typing import List

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
            Cmax=max(Cmax,t+e.q)
    return order,Cmax
