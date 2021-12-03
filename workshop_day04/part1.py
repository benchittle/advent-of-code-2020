""" 
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) OPTIONAL
 """

REQUIRED = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


with open("input.txt") as file:
    data = file.read().split("\n\n")

data = [p.replace("\n", " ") for p in data]

passports = []
for pString in data:
    fieldDict = {}
    for field in pString.split():
        name, value = field.split(":")
        fieldDict[name] = value
    passports.append(fieldDict)

count = 0
for pDict in passports:
    for req in REQUIRED:
        if req not in pDict:
            break
    else:
        count += 1

print(count)