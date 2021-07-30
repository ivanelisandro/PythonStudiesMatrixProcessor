import numpy as np

dimension = int(input())
fill_with = int(input())

if fill_with == 0:
    print(np.zeros((dimension, dimension)))
elif fill_with == 1:
    print(np.ones((dimension, dimension)))
