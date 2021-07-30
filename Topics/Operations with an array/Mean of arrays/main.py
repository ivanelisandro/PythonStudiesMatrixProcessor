import numpy as np


array = np.array([[[7, 8], [13, 9]], [[9, 5], [15, 14]]])
index = int(input())
print(array.mean(axis=index))
