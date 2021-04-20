import Load
from neh import NEHmodifications
from neh import NEH
from neh import Cmax
import TS
import Johnson

schedule = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(TS.neighbourhoods_generator(schedule, function="inverse", inverse_len=7))

functions = ["swap", "inverse", "insert"]
data = Load.read_datest("Data/data.txt")[2]
history = []
init = "sequence"
stop_func = "iter"
for function in functions:
    print(TS.Tabu_search(data, stop=stop_func, init_function=init,
                                   neighbourhoods_function=function))

print(history)