import numpy as np
import matplotlib.pyplot as plt
 
#生成数据
x=np.arange(0,40,0.01)#以0.1为单位，生成0到6的数据
y1=(1+np.sin(x)/x)
y2=(1-np.sin(x)/x)
z = np.linspace(0, 12 * np.pi, 13)
labels = map(lambda z: f"{z/np.pi}π", z)
#绘制图形
plt.rcParams['font.sans-serif']=['SimHei']#解决标题、坐标轴标签不能是中文的问题
plt.rcParams['axes.unicode_minus']=False#标题等默认是英文输出
plt.plot(x,y1,label='1+sinx/x',c='red')
plt.plot(x,y2,label='1-sinx/x',c='b')
# 画出 y=1 这条水平线
plt.axhline(1,c='g')
# plt.xlabel('X')
# plt.ylabel('Y')
plt.xticks(z, labels)
# plt.title('正弦余弦函数图像')
plt.legend()
plt.show()