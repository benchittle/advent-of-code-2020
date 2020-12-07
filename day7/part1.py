import re

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


##########################################################
# Recursive approach more like recursive not working gotem
##########################################################

'''def look_for(desired_colour, thisbag, mappings):
    flag = False
    for colour in thisbag:
        if colour == desired_colour:
            return True
        elif mappings[colour] is not None:
            flag = look_for(desired_colour, mappings[colour], mappings)
    return flag


for key in mappings:
    print(key, ":", mappings[key])

count = 0

for colour, contents in mappings.items():
    if contents is not None:
        if look_for("shiny gold", contents, mappings):
            count += 1
print(count)

'''


####################
# Iterative approach
####################

valid_bags = set()

# Make an initial pass and add any bags that contain the shiny gold bag directly
# to the set of valid bags.
for top_colour, contents in mappings.items():
    if contents is not None:
        if DESIRED_BAG in contents.keys():
            valid_bags.add(top_colour)

# Iterate over all the bags and add any bag that containing a valid bag to the
# set of valid bags until all valid bags have been added.
changed = True
while changed:
    startlen = len(valid_bags)

    # Iterate over all the bags.
    for top_colour, contents in mappings.items():
        if contents is not None:
            # Check each inner bag to see if it's valid.
            for inner_colour in contents:
                if inner_colour in valid_bags:
                    valid_bags.add(top_colour)
                    break

    changed = len(valid_bags) != startlen

print("Number of bags containing a {} bag: {}".format(DESIRED_BAG, len(valid_bags)))