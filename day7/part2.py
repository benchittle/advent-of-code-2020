import re


def count_bags_deep(current_bag, mappings):
    # Get the bags contained within this bag.
    contents = mappings[current_bag]

    count = 0
    if contents is not None:
        # For each inner bag, get the number of bags within it and apply it to
        # the total.
        for inner_bag, amt in contents.items():
            count += amt + amt * count_bags_deep(inner_bag, mappings)
    return count


DESIRED_BAG = "shiny gold"

with open("input.txt") as file:
    data = file.read().split("\n")

mappings = {}

for line in data:
    bag = re.match(r"\w+ \w+", line).group()
    mappings[bag] = {}

    contents = re.findall(r"(\d+) (\w+ \w+)", line)
    if contents is None:
        mappings[bag] = None
    else:
        for amt, kind in contents:
            mappings[bag][kind] = int(amt)

print("Number of bags in {}: {}".format(DESIRED_BAG, count_bags_deep(DESIRED_BAG, mappings)))