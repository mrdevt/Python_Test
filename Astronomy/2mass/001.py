import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
file_path="C:/Users/TWS/Desktop/mag1204.csv"
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
time_list=[]
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['HJD'] for row in reader]
    for i in column:
        if i not in time_list:
            time_list.append(i)
            # if i>'22:32:50':
            #     break
    print(len(time_list))
    # print(time_list)

# numpy
# data = np.loadtxt(file_path,delimiter=',')     #一定要有第二个参数，否则报错，因为csv文件里面是用,分割开的
# print(data.shape)    #（3600,5）
# print("-------------------------------------------")
# pandas
# df = pd.read_csv(file_path)
# print(df)
# data = np.array(df)
# print(data.shape)     #(3960, 5)

