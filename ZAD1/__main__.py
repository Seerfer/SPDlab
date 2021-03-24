import LoadData
import Johnson
import Cmax

data = LoadData.readData("data.txt")
print(Cmax.count_cmax(Johnson.multi_machines_Johnson(data[-1][0]), data[-1][0]))


