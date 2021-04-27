import Load
import Cmax

tasks = Load.readData("test.txt")
print(Cmax.Cmax(tasks))