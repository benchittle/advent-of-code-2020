import re, itertools, math

with open("input.txt") as file:
    data = sorted(map(int, file.read().split("\n")))

rating = data[-1] + 3

difs = {1:0, 2:0, 3:1}

for i, j in zip(data[:-1], data[1:]):
    difs[j - i] += 1

print(difs[3] * difs[1], difs)