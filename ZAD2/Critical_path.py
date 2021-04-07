#funkcja znajduje ścieżke krytyczną, napisana na podstawie funkcji obliczającej Cmax
def critical_path(sched, times):
    times = list((map(list, zip(*times))))
    crit_path = []
    crit_time = 0      # zmienna pomocnicza obliczajaca czas trwania sciezki krytycznej
    tmp = [[None for _ in range(len(times[0]))] for _ in range(len(times))]
    for i in range(0, len(times)):
        for j in range(len(times[0])):
            if i == 0:
                if j == 0:
                    tmp[i][j] = times[sched[i] - 1][j]
                    crit_path.append((sched[i], j+1))   # dodanie pierwszego wykonaywanego zadania do sciezki
                    crit_time += times[sched[i] - 1][j]     # zsumowanie aktualnego czasu wykonywania sciezki
                else:
                    tmp[i][j] = (tmp[i][j - 1] + times[sched[i] - 1][j])
            else:
                if j == 0:
                    tmp[i][j] = tmp[i - 1][j] + times[sched[i] - 1][j]
                else:
                    tmp[i][j] = max(tmp[i - 1][j], tmp[i][j - 1]) + times[sched[i] - 1][j]
                    if (tmp[i][j-1]) >= (tmp[i-1][j]):   #sprawdzenie, który krok jest dluzszy i bedzie brany pod uwage do sciezki
                        if ((tmp[i][j-1]) - (times[sched[i]-1][j-1])) == crit_time:  #sprawdzenie czy wybrany krok zaczyna się równo z zakończeniem poprzedniego na ścieżce
                            crit_path.append((sched[i], j))     #dodanie zadania do ścieżki
                            crit_time += times[sched[i] - 1][j-1]   #aktualizacja czasu
                    else:
                        if ((tmp[i-1][j]) - (times[sched[i-1]-1][j])) == crit_time: #sprawdzenie czy czas rozpoczecia zgadza sie z zakonczeniem poprzedniego
                            crit_path.append((sched[i-1], j+1))
                            crit_time += times[sched[i] - 1][j]
                    if i == len(times)-1:       # dodanie ostatniego wykonywanego zadania do sciezki
                        if j == len(times[0])-1:
                            if ((tmp[i][j]) - (times[i][j])) == crit_time:
                                crit_path.append((sched[i], j+1))
                                crit_time += times[i][j]
    return crit_path        # zwraca liste (zadanie, maszyna)

# funkcja szukajaca najdluzej trwajacego zadania na sciezce krytycznej
# potrzebne do pierwszego rozszerzenia
def longest_task_ex1(sched, times):
    crit_path = critical_path(sched, times) # oblicza sciezke krytyczna
    times = list((map(list, zip(*times))))
    max_time = 0
    task_with_max = 0
    for item in crit_path:  #petla po elementach sciezki
        task, machine = item
        time = times[task-1][machine-1]
        if time > max_time:    #sprawdzenie czy czas danego zadania jest najdluzszym czasem
            max_time = time
            task_with_max = task
    return task_with_max    # zwraca zadanie z najdluzszym czasem wykonywania na sciezce


# funkcja szukająca zadania, z największa sumą operacji na ściezce
# potrzebne do drugiego rozszerzenia
def task_with_biggest_sum_ex2(sched, times):
    crit_path = critical_path(sched, times) # obliczanie sciezki
    times = list((map(list, zip(*times))))
    biggest_sum_task = None
    sum = {}    #pusty słownik (zadanie:czas trwania)
    for item in crit_path:
        task, machine = item
        time = times[task - 1][machine - 1]
        if task in sum:
            sum[task] += time   # dodawanie czasów do wystepujących wczesniej zadań
        else:
            sum[task] = time    # dodawanie elementów do słownika
    if sum:
        biggest_sum_task = max(sum, key=sum.get)    # znalezienie zadania z najdłuzszym czasem trwania
    return biggest_sum_task # zwraca zadanie z największa suma


# funkcja znajdująca zadanie występujące najwiecej razy na ściezce
# potrzebna do trzeciego rozszerzenia
def most_operations_task_ex3(sched, times):
    crit_path = critical_path(sched, times)
    tasks = [] # pusta lista zadań
    task_most = 0
    most = 0
    for item in crit_path:
        task, machine = item
        tasks.append(task)  # dodanie zadania na liste
    for item in tasks:
        operations = tasks.count(item)  # zliczanie które zadanie wystąpilo najczęściej
        if operations > most:
            most = operations
            task_most = item
    return task_most    # zwraca zadanie wystepujące najwięcej razy na ścieżce krytycznej
