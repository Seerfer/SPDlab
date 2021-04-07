import NEH
import Load
import NEHmodifications
import tests
import Johnson
import Cmax

times = Load.readData("Data/data001v.txt")
print(NEH.neh(times))
print(NEHmodifications.neh_ext4(times))
print(NEHmodifications.neh_ext3(times))
print(NEHmodifications.neh_ext2(times))
print(NEHmodifications.neh_ext1(times))
