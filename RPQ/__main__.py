import Load
import schrage
import Carlier
import time
import Tabu
tasks = Load.readData("Data/in50.txt")

cr = Carlier.Carlier(10000000)
#
#
print(schrage.schrage_heapq(tasks))
# print(schrage.schrage_pmtn(tasks))
# print(schrage.schrage_pmtn(tasks))
# print(schrage.schrage_pmtn(tasks))
#
# start_time = time.time()
# Cmax,order = cr.carlier(tasks)
# execution_time = time.time() - start_time
# print('Carlier: ' + str(Cmax) + ' Czas: ' + str(execution_time))
#
start_time = time.time()
Cmax1,order1 = cr.carlier_heapq(tasks)
execution_time = time.time() - start_time
print('Carlier_heapq: ' + str(Cmax1) + ' Czas: ' + str(execution_time))



