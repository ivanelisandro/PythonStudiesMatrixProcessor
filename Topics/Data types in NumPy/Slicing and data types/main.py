import numpy as np

array = np.array([[212, 215, 434, 2, 0],
                  [6, 447, 0, 4, 143],
                  [10, 478, 601, 602, 3]], dtype=np.float64)

row = int(input())
items_step = int(input())
print(array[row, ::items_step].astype(np.int8))
