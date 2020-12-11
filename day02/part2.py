import re

count = 0

with open("input.txt") as file:
    for line in file:
        p1, p2 = map(int, re.findall(r"\d+", line))
        pwd = line[line.index(":") + 2:]
        letter = line[line.index(":") - 1]

        if pwd[p1 - 1] == letter or pwd[p2 - 1] == letter:
            if not (pwd[p1 - 1] == letter and pwd[p2 - 1] == letter):
                count += 1

print(count)