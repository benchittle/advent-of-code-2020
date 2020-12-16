# Original solution
with open("input.txt") as file:
    data = file.read().split(",")

said = list(map(int, data))

dsize = len(data)

while len(said) < 2020:
    print(len(said))
    if said[-1] in said[:-1]:
        said.append(list(reversed(said[:-1])).index(said[-1]) + 1)
    else:
        said.append(0)

print(said)
