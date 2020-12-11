with open("input.txt") as file:
    ops = []
    for line in file.read().split("\n"):
        action, val = line.split()
        ops.append((action, int(val)))

# Find all the lines with a 'jmp' or 'nop'.
lines_to_try = []
for line, (action, arg) in enumerate(ops):
    if action == "jmp" or action == "nop":
        lines_to_try.append(line)

ops_original = ops.copy()
size = len(ops)

for change in lines_to_try:
    # Undo the previous change.
    ops = ops_original.copy()
    # Switch the action to 'jmp' or 'nop' at the current line to be changed.
    old_op, val = ops[change]
    ops[change] = ("jmp", val) if old_op == "nop" else ("nop", val)

    acc = 0
    visited = set()
    line = 0
    while line not in visited:
        if line < size:
            visited.add(line)
            op, arg = ops[line]
            if op == "nop":
                line += 1
            elif op == "acc":
                acc += arg
                line += 1
            elif op == "jmp":
                line += arg
        else:
            print("Program terminated with acc={}\n"
                  "Line {} was modified (was '{}')".format(acc, change, old_op))
            break