import math

number = int(input())
logistic = 1 / (1 + math.exp(-number))
print(round(logistic, 2))
