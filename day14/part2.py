import re, itertools, collections


# Original solution
def apply_mask(mask, string):
    string = ['0'] * (len(mask) - len(string)) + list(string)
    floats = set()
    new = []
    for m, s in zip(mask, string):
        if m == "0":
            new.append(s)
        elif m == "1":
            new.append("1")
        else:
            new.append("X")

    for combo in itertools.combinations_with_replacement(('0', '1'), new.count("X")):
        for perm in set(itertools.permutations(combo)):
            perm = iter(perm)
            floats.add("".join([i if i != "X" else next(perm) for i in new]))

    return floats


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
        for addr in apply_mask(mask, bin(index)[2:]):
            memory[int(addr, 2)] = num

print(memory)

print(sum(memory.values()))
