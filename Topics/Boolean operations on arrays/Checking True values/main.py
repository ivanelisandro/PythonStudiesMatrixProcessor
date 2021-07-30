import numpy as np

a = int(input())
b = int(input())
c = int(input())
array = np.array([a, b, c])
print(np.all(array > 15))
