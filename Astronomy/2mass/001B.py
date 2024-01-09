import csv
import math
import numpy as np
from astropy.time import Time
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
file_path="D:\Git\Python_Test\Astronomy\\2mass\mag1204.csv"
R3=[]
R4=[]
R5=[]
R6=[]
R7=[]
R8=[]
R9=[]
R10=[]
HJD=[]
# x=[i for i in range(1,113)]
plt.figure(figsize=(30,20))
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    hjd = [row['HJD'] for row in reader]
    time=hjd[0:len(hjd):4][:112]
    for t in time:
        j=Time(t,format='isot')
        HJD.append(j)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['3*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R3.append(i)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['4*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R4.append(i)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['5*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R5.append(i)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['6.25*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R6.append(i)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['7*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R7.append(i)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['8*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R8.append(i)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['9*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R9.append(i)
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['10*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R10.append(i)

plt.scatter(x[0:112],R3[0:len(R3)],label='3R',)
plt.scatter(x[0:112],R4[0:len(R4)],c='c',label='4R')
plt.scatter(x[0:112],R5[0:len(R5)],c='b',label='5R')
plt.scatter(x[0:112],R6[0:len(R6)],c='g',label='6R')
plt.scatter(x[0:112],R7[0:len(R7)],c='r',label='7R')
plt.scatter(x[0:112],R8[0:len(R8)],c='m',label='8R')
plt.scatter(x[0:112],R9[0:len(R9)],c='y',label='9R')
plt.scatter(x[0:112],R10[0:len(R10)],c='k',label='10R')

plt.plot(x[0:112],R3[0:len(R3)],label='3R',)
plt.plot(x[0:112],R4[0:len(R4)],label='4R',c='c')
plt.plot(x[0:112],R5[0:len(R5)],c='b',label='5R')
plt.plot(x[0:112],R6[0:len(R6)],c='g',label='6R')
plt.plot(x[0:112],R7[0:len(R7)],c='r',label='7R')
plt.plot(x[0:112],R8[0:len(R8)],c='m',label='8R')
plt.plot(x[0:112],R9[0:len(R9)],c='y',label='9R')
plt.plot(x[0:112],R10[0:len(R10)],c='k',label='10R')
plt.xticks(np.arange(1, 113, 1), HJD)
plt.legend()
plt.rcParams['font.sans-serif']=['SimHei']
plt.xticks(range(0,len(HJD),1),rotation=45, ha='right')
plt.title("B-波段")
# 设置 x 和 y 轴名称
plt.xlabel('时间')
plt.ylabel('星等')
plt.savefig("D:\Git\Python_Test\Astronomy\\2mass\Figure-B.png")
plt.show()
