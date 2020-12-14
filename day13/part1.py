import re, itertools, collections


# Original solution
with open("input.txt") as file:
    data = file.read().split("\n")

timestamp = int(data[0])

ids = list(map(int, data[1].replace("x,", "").split(",")))
difs = []

for i in ids:
    time_left = i - timestamp % i
    difs.append((i, time_left))

print(difs)
shortest = min(difs, key=lambda x: x[1])

print(shortest[0] * shortest[1])