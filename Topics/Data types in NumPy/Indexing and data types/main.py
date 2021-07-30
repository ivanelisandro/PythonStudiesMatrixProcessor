import numpy as np

array = np.array([[0, 2, 1998],
                  [12, 0, 1212],
                  [21, 0, 0],
                  [7, 0, 2019]])
index = int(input())
print(array[index].astype(np.bool_))
