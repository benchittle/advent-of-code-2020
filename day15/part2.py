import re, itertools, collections

# Original solution
with open("input.txt") as file:
    data = file.read().split(",")


said = {int(data[i]) : i + 1 for i in range(len(data))}
prevsaid = {int(data[i]) : i + 1 for i in range(len(data) - 1)}
prev = int(data[-1])

turn = len(said) + 1

while turn <= 30000000:
    if prev in prevsaid:
        saying = turn - 1 - prevsaid[prev]
    else:
        saying = 0

    said[saying] = turn
    prevsaid[prev] = turn - 1
    prev = saying
    turn += 1

print(prev)
