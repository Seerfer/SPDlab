import NEH
import Load
import NEHmodifications
import tests
import Johnson
import Cmax

times = Load.readData("Data/tmp.txt")
print(NEH.neh(times))