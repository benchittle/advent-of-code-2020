import re

count = 0

with open("input.txt") as file:
    for line in file:
        lower, upper = map(int, re.findall(r"\d+", line))
        letter = line[line.index(":") - 1]

        if lower <= line.count(letter) - 1 <= upper:
            count += 1

print(count)

