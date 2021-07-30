import numpy as np

array = np.array([[-34, 2, 0],
                  [0, -4, 123],
                  [-201, 0, -3]], dtype=np.int64)

index_1 = int(input())
index_2 = int(input())

print(array[index_1].astype(np.str_))
print(array[index_2].astype(np.float64))
