import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
array_1 = np.array([[a, b], [c, d]])
array_2 = np.array([e, f])
result = array_1.T - array_2
print(result)
