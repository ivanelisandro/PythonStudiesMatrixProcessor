import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

array = np.array([[a, b], [c, d]])
rank = np.linalg.matrix_rank(array)
print(rank)
