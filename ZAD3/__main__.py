import Load
from neh import NEHmodifications
from neh import NEH
import TS

times = Load.readData("Data/tmp.txt")
print(TS.Tabu_search(times))
schedule = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(TS.neighbourhoods_generator(schedule))