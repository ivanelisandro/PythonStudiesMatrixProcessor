import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

arr = np.array([[a, b], [c, d]])
w, v = np.linalg.eig(arr)
print(w)
