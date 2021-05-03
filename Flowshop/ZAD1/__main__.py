import LoadData
import Johnson
import Cmax
import Gantt
import AllPosiblities
data = LoadData.readData("data.txt")


Gantt.gantt(data[1][2], data[1][0])