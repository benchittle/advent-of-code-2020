import re, itertools, collections

def apply_mask(mask, string):
    string = ['0'] * (len(mask) - len(string)) + list(string)
    new = []
    for m, s in zip(mask, string):
        if m == "X":
            new.append(s)
        else:
            new.append(m)
    return "".join(new)





# Original solution
with open("input.txt") as file:
    data = file.read().split("\n")

memory = {}
mask = None

for line in data:
    values = line.split()
    if values[0] == "mask":
        mask = values[2]
    else:
        index = int(re.findall(r"\d+", values[0])[0])
        num = int(values[2])
        memory[index] = apply_mask(mask, bin(num)[2:])

print(memory)

print(sum([int(i, 2) for i in memory.values()]))
