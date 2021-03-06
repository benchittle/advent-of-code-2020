# Original
count = 0
with open("input.txt") as file:
    filestr = file.read()

data = filestr.split("\n\n")

for i, group in enumerate(data):
    responses = set()
    for person in group.split("\n"):
        for letter in person:
            responses.add(letter)
    count += len(responses)

print(count)


# One lienr
with open("input.txt") as file:
    print(sum((len(set.union(*(set(person) for person in group.split("\n")))) for group in file.read().split("\n\n"))))



