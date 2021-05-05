import Load
import Cmax
import schrage
import schrage_pmtn
from Heapq import Heapq
import schrage_pmtn

tasks = Load.readData("test.txt")
print(schrage.schrage(tasks))
print(schrage.schrage_heapq(tasks))
print(schrage_pmtn.schrage_pmtn(tasks))
print(schrage_pmtn.schrage_pmtn_heapq(tasks))