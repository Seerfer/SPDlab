import Load
import schrage

tasks = Load.readData("Data/in200.txt")
print(schrage.schrage(tasks))
print(schrage.schrage_heapq(tasks))
print(schrage.schrage_pmtn(tasks))
print(schrage.schrage_pmtn_heapq(tasks))