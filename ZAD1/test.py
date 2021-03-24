import LoadData
import random
import time
import AllPosiblities
import matplotlib.pyplot as plt
import Johnson

#Przegląd zupełny w zależnosci od zadan
def run_test1():
    times = []
    tasks = []
    for i in range(3, 12):
        dataset = [[random.randint(1, 15) for _ in range(i)] for _ in range(4)]
        start = time.perf_counter()
        AllPosiblities.all_posibilities(dataset)
        end = time.perf_counter()

        print(end-start)
        times.append(end-start)
        tasks.append(i)

    plt.plot(tasks, times)
    plt.ylabel("Czas w sekundach")
    plt.xlabel("Liczba zadań")
    plt.title("Przegląd zupełny przy stałej liczbie maszyn")
    plt.show()

#Przegląd zupełny w zależnosci od maszyn
def run_test2():
    times = []
    tasks = []
    for i in range(3, 100):
        dataset = [[random.randint(1, 15) for _ in range(6)] for _ in range(i)]
        start = time.perf_counter()
        AllPosiblities.all_posibilities(dataset)
        end = time.perf_counter()

        print(end - start)
        times.append(end - start)
        tasks.append(i)

    plt.plot(tasks, times)
    plt.ylabel("Czas w sekundach")
    plt.xlabel("Liczba maszyn")
    plt.title("Przegląd zupełny przy stałej liczbie zadań")
    plt.show()

#Johnson w zależnosci od zadan
def run_test3():
    times = []
    tasks = []
    for i in range(3, 1000):
        dataset = [[random.randint(1, 15) for _ in range(i)] for _ in range(4)]
        start = time.perf_counter()
        Johnson.multi_machines_Johnson(dataset)
        end = time.perf_counter()

        print(end-start)
        times.append(end-start)
        tasks.append(i)

    plt.plot(tasks, times)
    plt.ylabel("Czas w sekundach")
    plt.xlabel("Liczba zadań")
    plt.title("Algorytm Johnsona przy stałej liczbie maszyn")
    plt.show()

#Johnson zupełny w zależnosci od maszyn
def run_test4():
    times = []
    tasks = []
    for i in range(3, 500):
        dataset = [[random.randint(1, 15) for _ in range(6)] for _ in range(i)]
        start = time.perf_counter()
        Johnson.multi_machines_Johnson(dataset)
        end = time.perf_counter()

        print(end - start)
        times.append(end - start)
        tasks.append(i)

    plt.plot(tasks, times)
    plt.ylabel("Czas w sekundach")
    plt.xlabel("Liczba maszyn")
    plt.title("Algorytm Johnsona przy stałej liczbie zadań")
    plt.show()
