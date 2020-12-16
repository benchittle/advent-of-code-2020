import re

# Original solution
def range_to_set(range_str):
    start, stop = map(int, range_str.split("-"))
    return set(range(start, stop + 1))



with open("input.txt") as file:
    data = file.read().split("\n\n")

my_ticket = data[1].split("\n")[1]

fields = data[0].split("\n")
fields = {re.match(r"([\w ]+):", f).group(1) : re.findall(r"\d+-\d+", f) for f in fields}

# Determine the set of all valid numbers for each field.
valid_nums_by_field = {f : set.union(*(range_to_set(s) for s in fields[f])) for f in fields}

# Determine the set of all valid numbers.
all_valid_nums = set.union(*valid_nums_by_field.values())

nearby = [my_ticket] + data[2].split("\n")[1:]

valid_tickets = []
for ticket in nearby:
    ticket = tuple(map(int, ticket.split(",")))
    for num in ticket:
        if num not in all_valid_nums:
            break
    else:
        valid_tickets.append(ticket)

# The columns of the nearby ticket input
entry_columns = {i : set((valid_tickets[j][i] for j in range(len(valid_tickets)))) for i in range(len(valid_tickets[0]))}

# The potential field(s) that each column of entries could map to.
potential_fields = {col : set() for col in entry_columns}

for col, entries in entry_columns.items():
    for field, valid_entries in valid_nums_by_field.items():
        if entries.issubset(valid_entries):
            potential_fields[col].add(field)

# For mapping each column to the corresponding field name.
fields_to_cols = {}
#
while len(fields_to_cols) != len(fields) - 1:
    for col, pot_fields in potential_fields.items():
        field = pot_fields.difference(set.union(*(pfs for c, pfs in potential_fields.items() if c != col)))

        if len(field) == 1:
            fields_to_cols[field.pop()] = col
            potential_fields.pop(col)
            break
        elif len(field) > 1:
            print("MORE THAN ONE")

fields_to_cols[list(potential_fields.values())[0].pop()] = list(potential_fields.keys())[0]


product = 1
for field in fields:
    if field.startswith("departure"):
        product *= int(my_ticket.split(",")[fields_to_cols[field]])

print(product)