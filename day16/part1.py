import re

# Original solution

def range_to_set(range_str):
    start, stop = map(int, range_str.split("-"))
    return set(range(start, stop + 1))



with open("input.txt") as file:
    data = file.read().split("\n\n")


fields = data[0].split("\n")
fields = {re.match(r"([\w ]+):", f).group(1) : re.findall(r"\d+-\d+", f) for f in fields}

# Determine the set of all valid numbers.
ranges = [r for f in fields.values() for r in f]
valid_nums = set.union(*map(range_to_set, ranges))

nearby = data[2].split("\n")[1:]

invalid_sum = 0
for ticket in nearby:
    for num in map(int, ticket.split(",")):
        if num not in valid_nums:
            invalid_sum += num
            break

print(invalid_sum)