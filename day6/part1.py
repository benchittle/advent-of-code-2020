ans_sets = []
count = 0

with open("input.txt") as file:
    filestr = file.read()

data = filestr.split("\n\n")

for i, group in enumerate(data):
    responses = set()
    for person in group.split("\n"):
        for letter in person:
            responses.add(letter)
    ans_sets.append(responses)
    count += len(responses)

print(count)
