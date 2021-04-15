import Load
from neh import NEHmodifications
from neh import NEH
import TS

times = Load.readData("Data/tmp.txt")
print(NEH.neh(times)[0])
print(TS.neighbours(NEH.neh(times)[0], function="insert"))