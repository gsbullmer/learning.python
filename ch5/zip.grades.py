grades = [18, 23, 30, 27, 15, 9, 22]
avgs = [22, 21, 29, 24, 18, 18, 24]
print(list(zip(avgs, grades)))
# [(22, 18), (21, 23), (29, 30), (24, 27), (18, 15), (18, 9), (24, 22)]
print(list(map(lambda *a: a, avgs, grades)))    # equivalent to zip
# [(22, 18), (21, 23), (29, 30), (24, 27), (18, 15), (18, 9), (24, 22)]
