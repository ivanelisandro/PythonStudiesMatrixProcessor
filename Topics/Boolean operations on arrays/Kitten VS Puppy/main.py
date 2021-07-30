import numpy as np

list_1 = []
for i in input().split():
    list_1.append(int(i))
list_2 = input().split()
list_3 = input().split()

a = np.array(list_1)
b = np.array(list_2)
c = np.array(list_3)
for word in np.where(a >= 0, b, c):
    print(word)
