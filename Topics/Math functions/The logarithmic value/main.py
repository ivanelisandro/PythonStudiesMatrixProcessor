import math

number = int(input())
base = int(input())
result = None

if base <= 0 or base == 1:
    result = math.log(number)
else:
    result = math.log(number, base)

if result:
    print(round(result, 2))
