# from astropy.time import Time
# t1 = Time('2021-04-01T06:50:54',format='isot')
# t2 = Time('59376.8368',format='mjd')
# print(t1.mjd)
# print(t1.jd)
# # print(t1.hjd)
# print(t2.mjd)
# print(t2.jd)

import csv
import math
import numpy as np
import pandas as pd
from astropy.time import Time
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
file_path="D:\Git\Python_Test\Astronomy\\2mass\mag1204.csv"
R3=[]
time=[]
x=[i for i in range(112)]
print(len(x))
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    hjd = [row['HJD'] for row in reader]
    print(hjd)
    print(len(hjd))
    time=hjd[0:len(hjd):4][:112]
    print(len(time))
    print(time)
    print(type(time[0]))
    # reader = csv.DictReader(csvfile)
    # r=  [row['3*R'] for row in reader]
    # print(len(r))
    # R3=r[0:len(r):4][:112]
    # print(len(R3))
    # # print(R3)
    # plt.scatter(x,R3)
    # plt.show()

# years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# turnovers = [0.5, 9.36, 52, 191, 350, 571, 912, 1027, 1682, 2135, 2684]
# squares = [math.pow(year-2008, 3.3) for year in years]
# powers = [math.pow(2, year-2008) for year in years]
# plt.figure(figsize=(10, 15), dpi=100)
# size = list()
# for tur in turnovers:
#     size.append(tur) if tur > 100 else size.append(100)
# plt.xticks(range(2008, 2020, 1))
# plt.yticks(range(0, 3200, 200))
# plt.scatter(years, turnovers, c=np.random.randint(0, 50, 11), s=size, label='成交额')
# plt.plot(years, squares, color='red', label='x^3.3')
# plt.plot(years, powers, color='blue', label='2^n')
# plt.legend(loc='best', fontsize=16, markerscale=0.5)
# plt.xlabel("年份", fontdict={'size': 16})
# plt.ylabel("成交额", fontdict={'size': 16})
# plt.title("历年天猫双11总成交额", fontdict={'size': 20})
# plt.show()

# import csv
# from astropy.time import Time
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# file_path="C:/Users/TWS/Desktop/mag1204.csv"
# with open(file_path,'r',encoding = 'utf-8') as f:
#     print(f.readline())
# df = pd.read_csv(file_path,encoding="utf-8")
# print(df)
# data = np.loadtxt(open(file_path,"rb"),delimiter=",",skiprows=n,usecols=[2,3])
# 读取某行
# csv = csv.reader(open(file_path))
# i= 0
# print(type(csv))
# for row in csv:
# 	if i % 2 == 0:
# 	    print(row)
# print("-------------------------------------------")
# 读取某列
# time_list=[]
# with open(file_path, "rt") as csvfile:
#     reader = csv.DictReader(csvfile)
#     column = [row['HJD'] for row in reader]
#     k=0
#     for i in column:
#         if i not in time_list and k<112:
#             j=Time(i,format='isot')
#             time_list.append(j)
#             k=k+1
#     print(len(time_list))
#     # print(time_list)
# time=[]
# for t in time_list:
#     time_list.append(t)
#     # print(t,end='\n')
# for t in time:
#     print(t, end='\n')
# time_list=[]
# for i in time_list1:
#     if i not in time_list:
#         time_list.append(i)
# print(len(time_list))

# numpy
# data = np.loadtxt(file_path,delimiter=',')     #一定要有第二个参数，否则报错，因为csv文件里面是用,分割开的
# print(data.shape)    #（3600,5）
# print("-------------------------------------------")
# pandas
# df = pd.read_csv(file_path)
# print(df)
# data = np.array(df)
# print(data.shape)     #(3960, 5)

