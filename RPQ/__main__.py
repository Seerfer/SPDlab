import Load
import schrage
import Carlier
import time
tasks = Load.readData("Data/in50.txt")

cr = Carlier.Carlier(10000000)



print(schrage.schrage_pmtn(tasks))
print(schrage.schrage_pmtn(tasks))
print(schrage.schrage_pmtn(tasks))

cr.carlier(tasks)