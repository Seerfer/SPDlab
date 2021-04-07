import Load
import time
import NEH
import NEHmodifications
import Johnson
import Cmax
import csv
import random

def run_tests_from_dataset():
    datas = Load.read_datest("Data/data.txt")
    #times
    neh = []
    neh1 = []
    neh2 = []
    neh3 = []
    neh4 = []
    johnson = []

    #cmax
    neh_c = []
    neh1_c = []
    neh2_c = []
    neh3_c = []
    neh4_c = []
    johnson_c = []


    machines = []
    tasks = []
    i = 1
    for times in datas:
        print(f"Reading data {i}")
        machines.append(len(times[0]))
        tasks.append(len(times))

        print("Test NEH")
        start = time.perf_counter()
        neh_c.append(NEH.neh(times)[1])
        end = time.perf_counter()
        neh.append(start-end)

        print("Test NEH4")
        start = time.perf_counter()
        neh4_c.append(NEHmodifications.neh_ext4(times)[1])
        end = time.perf_counter()
        neh4.append(start - end)

        print("Test Johnoson")
        start = time.perf_counter()
        tmp = Cmax.count_cmax(Johnson.multi_machines_Johnson(times), times)
        end = time.perf_counter()
        johnson_c.append(tmp)
        johnson.append(start - end)

        print("Test NEH3")
        start = time.perf_counter()
        neh3_c.append(NEHmodifications.neh_ext3(times)[1])
        end = time.perf_counter()
        neh3.append(start - end)

        print("Test NEH2")
        start = time.perf_counter()
        neh2_c.append(NEHmodifications.neh_ext2(times)[1])
        end = time.perf_counter()
        neh2.append(start - end)

        print("Test NEH1")
        start = time.perf_counter()
        neh1_c.append(NEHmodifications.neh_ext1(times)[1])
        end = time.perf_counter()
        neh1.append(start - end)

        i = i+1
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Machines", "Tasks", "neh time", "neh cmax", "neh1 time", "neh1 cmax", "neh2 time", "neh2 cmax",
                         "neh3 time", "neh3 cmax", "neh4 time", "neh4 cmax", "Johnson time", "Johnson cmax"])
        for i in range(len(datas)):
            writer.writerow([machines[i], tasks[i], neh[i], neh_c[i], neh1[i], neh1_c[i], neh2[i], neh2_c[i],
                             neh3[i], neh3_c[i], neh4[i], neh4_c[i]])


def random_test():

    tasks = [5, 10, 15, 20, 50, 80, 120, 150]
    machines = [10]

    with open('ZAD2/results_tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tasks", "Machines", "Johnsoon time", "Johnson cmax", "neh time", "neh cmax",
                        "neh1 time", "neh1 cmax", "neh2 time", "neh2 cmax", "neh3 time", "neh3 cmax",
                        "neh4 time", "neh4 cmax"])
        for number in tasks:
            for machine in machines:
                neh = []
                neh1 = []
                neh2 = []
                neh3 = []
                neh4 = []
                johnson = []

                # cmax
                neh_c = []
                neh1_c = []
                neh2_c = []
                neh3_c = []
                neh4_c = []
                johnson_c = []
                for i in range(5):
                    times = [[random.randint(1, 15) for _ in range(machine)] for _ in range(number)]

                    print(f"{machine} {number}")

                    start = time.perf_counter()
                    neh_c.append(NEH.neh(times)[1])
                    end = time.perf_counter()
                    neh.append(end - start)

                    start = time.perf_counter()
                    neh4_c.append(NEHmodifications.neh_ext4(times)[1])
                    end = time.perf_counter()
                    neh4.append(end - start)

                    start = time.perf_counter()
                    tmp = Cmax.count_cmax(Johnson.multi_machines_Johnson(times), list((map(list, zip(*times)))))
                    end = time.perf_counter()
                    johnson_c.append(tmp)
                    johnson.append(end - start)

                    start = time.perf_counter()
                    neh3_c.append(NEHmodifications.neh_ext3(times)[1])
                    end = time.perf_counter()
                    neh3.append(end - start)

                    start = time.perf_counter()
                    neh2_c.append(NEHmodifications.neh_ext2(times)[1])
                    end = time.perf_counter()
                    neh2.append(end - start)

                    start = time.perf_counter()
                    neh1_c.append(NEHmodifications.neh_ext1(times)[1])
                    end = time.perf_counter()
                    neh1.append(end - start)

                writer.writerow([number, machine, sum(johnson)/len(johnson), sum(johnson_c)/len(johnson_c), sum(neh)/len(neh), sum(neh_c)/len(neh_c),
                                 sum(neh1)/len(neh1), sum(neh1_c)/len(neh1_c), sum(neh2)/len(neh2), sum(neh2_c)/len(neh2_c),
                                 sum(neh3)/len(neh3), sum(neh3_c)/len(neh3_c), sum(neh4)/len(neh4_c), sum(neh4_c)/len(neh4_c)])

