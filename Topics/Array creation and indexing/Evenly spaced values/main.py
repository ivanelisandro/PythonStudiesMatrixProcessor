import numpy as np

start = int(input())
stop = int(input())
quantity = int(input())
array = np.linspace(start, stop, num=quantity)

print(array[-2])
