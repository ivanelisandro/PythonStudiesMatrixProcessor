import numpy as np

x = int(input())
y = int(input())
z = int(input())
array = np.array([x, y, z])
print(array.max())
print(array.argmax())
