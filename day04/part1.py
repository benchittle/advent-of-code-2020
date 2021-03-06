import re

REQ_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
COLOURS = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
count = 0

with open("input.txt") as file:
    data = file.read().split("\n\n")
    data = [i.replace("\n", " ") for i in data]

for group in data:
    fields = {i[:3] : i[4:] for i in group.split(" ")}

    for i in REQ_FIELDS:
        if i not in fields.keys():
            break
    else:
        count += 1
print(count)