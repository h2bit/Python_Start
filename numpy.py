# https://blog.csdn.net/cxmscb/article/details/54583415
import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=int)
a = np.array((1, 2, 3, 4, 5), dtype=int)
a = np.arange(6)  # 开区间
a = np.arange(1, 6, 2)
a = np.arange(15).reshape(3, 5)
a = np.linspace(0, 180, 7)

a = np.random.rand(2, 3)
a = np.empty((2, 3), dtype=int)
a = np.zeros((2, 3), dtype=int)
a = np.ones((2, 3), dtype=int)
a = np.identity(3)

k = np.arange(9)  # [0,1,....8]
m = k.reshape((3, 3))
# print(m)
a = m.T

a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
print(a > b)
print(a.ndim)
print(a.shape)

# 'where函数的嵌套使用'
y1 = np.array([-1, -2, -3, -4, -5, -6])
y2 = np.array([1, 2, 3, 4, 5, 6])
y3 = np.zeros(6)
cond = np.array([1, 2, 3, 4, 5, 6])
x = np.where(cond > 5, y3, np.where(cond > 2, y1, y2))
print(x)  # [ 1.  2. -3. -4. -5.  0.]
