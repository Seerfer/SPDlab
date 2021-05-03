import Load
import Cmax
import schrage
import schrage_pmtn
tasks = Load.readData("test.txt")


print(schrage.schrage(tasks))
print(schrage_pmtn.schrage_pmtn(tasks))