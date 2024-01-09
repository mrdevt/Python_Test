import csv
import numpy as np
from astropy.time import Time
import matplotlib.pyplot as plt
file_path="D:\Git\Python_Test\Astronomy\\2mass\mag20231203.dat"
x=[i for i in range(1,113)]
def Read(n):
    R=[]
    with open(file_path, "rt") as csvfile:
        reader = csv.reader(csvfile)
        r = [row[n] for row in reader]
        for r in (r [0:len(r):4][112:224]):
            i=float(r)
            R.append(i)
        return R
with open(file_path, "rt") as csvfile:
    HJD=[]
    reader = csv.DictReader(csvfile)
    hjd = [row['HJD'] for row in reader]
    time=hjd[0:len(hjd):4][224:]
    for t in time:
        j=Time(t,format='isot')
        HJD.append(j)
plt.plot(x[0:len(x)],(Read(0))[0:len(Read(0))],label='3R',)
plt.plot(x[0:len(x)],(Read(1))[0:len(Read(1))],label='4R',c='c')
plt.plot(x[0:len(x)],(Read(2))[0:len(Read(2))],c='b',label='5R')
plt.plot(x[0:len(x)],(Read(3))[0:len(Read(3))],c='g',label='6R')
plt.plot(x[0:len(x)],(Read(4))[0:len(Read(4))],c='r',label='7R')
plt.plot(x[0:len(x)],(Read(5))[0:len(Read(5))],c='m',label='8R')
plt.plot(x[0:len(x)],(Read(6))[0:len(Read(6))],c='y',label='9R')
plt.plot(x[0:len(x)],(Read(7))[0:len(Read(7))],c='k',label='10R')

plt.xticks(np.arange(1, 113, 1), HJD)
plt.legend()
plt.rcParams['font.sans-serif']=['SimHei']
plt.xticks(range(0,len(HJD),1),rotation=45, ha='right')
plt.title("V-波段")
# 设置 x 和 y 轴名称
plt.xlabel('时间')
plt.ylabel('星等')
# plt.savefig("D:\Git\Python_Test\Astronomy\\2mass\Figure-V.png")
plt.show()