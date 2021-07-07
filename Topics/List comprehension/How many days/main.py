seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
full_days = [int(s / (60 * 60 * 24)) for s in seconds]
print(full_days)
