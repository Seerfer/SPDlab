import Load
from neh import NEHmodifications
from neh import NEH
from neh import Cmax
import TS
import Johnson

schedule = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data = TS.neighbourhoods_generator(schedule, function="inverse,swap", inverse_len=3)
set_ = set(tuple(i) for i in data)

print(len(data))
print(len(set_))

