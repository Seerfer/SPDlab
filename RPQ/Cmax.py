def cmax(tasks_list, schedule):
    tasks = []
    for i in schedule:
        for task in tasks_list:
            if task.id == i:
                tasks.append(task)
    S = [tasks[0].r]
    for i in range(1, len(tasks)):
        previous = tasks[i - 1]
        current = tasks[i]
        S.append(max(current.r, S[i - 1] + previous.p))
    C = []
    for start, task in zip(S, tasks):
        C.append(start + task.p)
    Cq = []
    for completion, task in zip(C, tasks):
        Cq.append(completion + task.q)
    return max(Cq)