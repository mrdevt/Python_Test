import matplotlib.pyplot as plt 
x_values = list(range(1, 1001)) 
y_values = [x**2 for x in x_values] 
# 删除数据点的轮廓
# 要修改数据点的颜色，可向scatter()传递参数c，
# plt.scatter(x_values, y_values, c =(0.8, 0.8, 0.8),edgecolor='none', s=40)
# 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色
# 映射用于突出数据的规律，例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显
# 示较大的值。
# 我们将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。这些代
# 码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色，
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
 edgecolor='none', s=40) 
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14) 
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000]) 
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight') 