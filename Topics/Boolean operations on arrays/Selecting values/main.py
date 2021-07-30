import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

array = np.array([a, b, c, d])
print(array[np.where(array >= 45)])
