import Load
import time
import NEH
import NEHmodifications
import Johnson

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

for times in datas:
    machines.append(len(times[0]))
    tasks.append(len(times))
    start = time.perf_counter()
    neh_c.append(NEH.neh(times)[1])
    end = time.perf_counter()
    neh.append(start-end)

    start = time.perf_counter()
    neh4_c.append(NEHmodifications.neh_ext4(times)[1])
    end = time.perf_counter()
    neh4.append(start - end)

    start = time.perf_counter()
    Johnson.multi_machines_Johnson(times)
    end = time.perf_counter()
    neh4.append(start - end)
