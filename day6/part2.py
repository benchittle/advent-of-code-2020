count = 0

with open("input.txt") as file:
    filestr = file.read()

data = filestr.split("\n\n")

for group in data:
    count += len(set.intersection(*[set(response) for response in group.split("\n")]))
print(count)


