with open("input.txt") as file:
    ops = []
    for line in file.read().split("\n"):
        action, val = line.split()
        ops.append((action, int(val)))

visited = set()
line = 0
acc = 0
while line not in visited:
    visited.add(line)
    op, arg = ops[line]
    if op == "nop":
        line += 1
    elif op == "acc":
        acc += arg
        line += 1
    elif op == "jmp":
        line += arg

print("acc={} when the program began repeating itself".format(acc))
