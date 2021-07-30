import math

side = int(input())
area = 2 * math.sqrt(3) * pow(side, 2)
volume = (1 / 3) * math.sqrt(2) * pow(side, 3)
print(round(area, 2), round(volume, 2))
