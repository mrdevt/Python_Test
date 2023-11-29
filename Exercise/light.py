import numpy as np
import matplotlib as plt

# 生成时间序列数据
time = np.linspace(0, 10,100)  # 时间范围为0到10，总共100个时间点
flux = np.sin(time) + np.random.normal(0, 0.1, 100)  # 生成带有噪声的光变曲线

# 绘制光变曲线
plt.figure(figsize=(8, 4))
plt.plot(time, flux, 'b-', label='Flux')
plt.xlabel('Time')
plt.ylabel('Flux')
plt.title('Light Curve')
plt.legend()
plt.grid(True)
plt.show()
