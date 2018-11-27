import matplotlib.pyplot as plt
import math
import numpy as np

# 设置图表标题,并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

t_values = np.arange(-10, 10, 0.1);
x_values = [math.cos(t)*5 + math.cos(2*t) / 2 + math.cos(3*t) / 15 + math.cos(4*t) / 8 + 20 for t in t_values]
y_values = [math.sin(t)*2 + math.cos(2*t) * 0.3 + math.sin(3*t) * 1.2 + math.sin(4*t) / 8 - 10 for t in t_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
edgecolor='none', s=40)

plt.show()
