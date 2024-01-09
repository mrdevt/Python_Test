
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
#创建画布
fig = plt.figure(figsize=(8, 8))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)  
#将绘图区对象添加到画布中
fig.add_axes(ax)
#通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
#ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0,0)
#给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("->", size = 1.0)
#添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right") 
#生成数据
x=np.arange(0,60,0.001)#以0.001为单位，生成0到60的数据
y1=(1+np.sin(x)/x)
y2=(1-np.sin(x)/x)
z = np.linspace(0, 19 * np.pi,20)
labels = map(lambda z: (f"{int(z/np.pi)}π"), z)
#绘制图形
plt.rcParams['font.sans-serif']=['SimHei']#解决标题、坐标轴标签不能是中文的问题
plt.rcParams['axes.unicode_minus']=False#标题等默认是英文输出
plt.title("P",  loc="left")
plt.plot(x,y1,label='1+sinx/x',c='r')
plt.plot(x,y2,label='1-sinx/x',c='b')
# 画出 y=1 这条水平线
plt.axhline(1,c='g')
# plt.xlabel('X')
# plt.ylabel('Y')
plt.xticks(z, labels)
# plt.title('')
import csv
R3=[]
l=[i for i in range(1,113)]
file_path="D:\Git\Python_Test\Astronomy\\2mass\mag1204.csv"
with open(file_path, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    r = [row['3*R'] for row in reader]
    for r in (r [0:len(r):4][:112]):
        i=float(r)
        R3.append(i)
plt.scatter(l[0:len(l)],R3[0:len(R3)],label='3R',)
plt.legend()
plt.show()