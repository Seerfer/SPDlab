import Load
from neh import NEHmodifications
from neh import NEH
times = Load.readData("Data/tmp.txt")
print(NEH.neh(times)[0])