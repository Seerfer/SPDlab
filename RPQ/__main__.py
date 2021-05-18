import Load
import schrage
import Carlier
import time
tasks = Load.readData("Data/in200.txt")

cr = Carlier.Carlier(10000000)

start_time = time.time()
Cmax,order = cr.carlier(tasks)
execution_time = time.time() - start_time
print('Carlier: ' + str(Cmax) + ' Czas: ' + str(execution_time))

start_time = time.time()
Cmax1,order1 = cr.carlier_heapq(tasks)
execution_time = time.time() - start_time
print('Carlier_heapq: ' + str(Cmax) + ' Czas: ' + str(execution_time))