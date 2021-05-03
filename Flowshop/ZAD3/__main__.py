import Load
from neh import NEHmodifications
from neh import NEH
from neh import Cmax
import TS
import Johnson
data = Load.readData("Data/tmp.txt")
TS.Tabu_search(data)
