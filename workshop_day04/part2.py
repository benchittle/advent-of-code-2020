
""" 
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Count ry ID) - ignored, missing or not.
    """
import re

# A set (like a list, but without order preserved) of the valid eye colours
# We use a set because it's faster to check whether a set contains an element
# than a list (though we could use a list here since we have so few elements)
EYE_COLOURS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def check(passport):
    if not (1920 <= int(passport["byr"]) <= 2002):
        return False
    if not (2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not (2020 <= int(passport["eyr"]) <= 2030):
        return False
    
    # Regex expression: identify a person's height by first looking at the
    # digits: ^(\d+)
    #   ^ indicates the string must start here
    #   () indicate that we want to extract whatever matches the contents of
    #      the expression in parentheses for later as part of the match variable
    #   \d indicates matching any digit from 0 to 9
    #   +  indicates that any number of digits can be matched
    # Then look at the unit
    #   |  indicates 'or', so the unit following the numbers must be either cm 
    #      or in 
    pattern = re.compile("^(\d+)(cm|in)$")
    match = pattern.match(passport["hgt"])
    if match:
        height, unit = match.groups()
        height = int(height)
        if (unit == "cm") and (not (150 <= height <= 193)):
            return False
        elif (unit == "in") and (not (59 <= height <= 76)):
            return False
    else:
        return False
    
    pattern = re.compile("^#[0-9a-f]{6}$")
    if not pattern.match(passport["hcl"]):
        return False

    if not passport["ecl"] in EYE_COLOURS:
        return False
    
    pattern = re.compile("^\d{9}$")
    if not pattern.match(passport["pid"]):
        return False

    return True



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
        if check(pDict):
            count += 1

print(count)