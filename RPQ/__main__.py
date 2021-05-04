import Load
import Cmax
import schrage
import schrage_pmtn
from Heapq import Heapq

tasks = Load.readData("test.txt")
kolejka = Heapq(tasks=tasks)
print(kolejka)

#print(schrage.schrage(tasks))
#print(schrage_pmtn.schrage_pmtn(tasks))