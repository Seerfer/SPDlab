import Load
from neh import NEHmodifications
from neh import NEH
from neh import Cmax
import TS
import Johnson

schedule = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(TS.neighbourhoods_generator(schedule, function="inverse", inverse_len=7))


times = Load.readData("Data/tmp.txt")
print(TS.Tabu_search(times))
