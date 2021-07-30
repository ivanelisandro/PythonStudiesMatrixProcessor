import math

degrees = int(input())
radians = math.radians(degrees)

cotangent = 1 / math.tan(radians)

print(round(cotangent, 10))
