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
        if ((1920 <= int(fields["byr"]) <= 2002)
                and (2010 <= int(fields["iyr"]) <= 2020)
                and (2020 <= int(fields["eyr"]) <= 2030)
                and (fields["ecl"] in COLOURS)
                and ((fields["hgt"][-2:] == "cm" and 150 <= int(fields["hgt"][:-2]) <= 193)
                      or (fields["hgt"][-2:] == "in" and 59 <= int(fields["hgt"][:-2]) <= 76))
                and (re.match("^#[a-f\d]{6}", fields["hcl"]) is not None)
                and (len(fields["pid"]) == 9)):
            count += 1
print(count)