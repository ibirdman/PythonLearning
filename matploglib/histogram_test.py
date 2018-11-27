import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def Histogram_demo():
    # set u and &
    mean = 100
    sigma = 10

    # produce normal distribution , 10000个数
    x = mean + sigma * np.random.randn(10000)

    num_bins = 50  # 共50个格子
    # 直方图函数， normed=1即和为1,
    # 返回50个概率、直方块左边线的x值、各个方块对象
    n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='yellow', alpha=0.5)
    y = mlab.normpdf(bins, mean, sigma)  # 一条逼近的曲线

    plt.plot(bins, y, "r--")
    plt.title("Histogram of XXX: $\mu=100$, $\sigma=10$")
    plt.xlabel("x-label")
    plt.ylabel("y-label")
    plt.grid()
    plt.subplots_adjust(left=0.15)
    plt.savefig("Histogram_demo.png")
    plt.show()


Histogram_demo()
