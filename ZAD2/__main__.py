import NEH
import Load
import NEHmodifications


sched = [2, 3, 1]
datas = Load.read_datest("Data/data.txt")

times = datas[8]
print(NEH.neh(times),"zwykly")
print(NEHmodifications.neh_ext1(times), "1 mod")
print(NEHmodifications.neh_ext2(times), "2 mod")
print(NEHmodifications.neh_ext3(times), "3 mod")
print(NEHmodifications.neh_ext4(times), "4 mod")