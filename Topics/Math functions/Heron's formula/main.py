import math

a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
square = p * (p - a) * (p - b) * (p - c)
s = math.sqrt(square)
print(s)
