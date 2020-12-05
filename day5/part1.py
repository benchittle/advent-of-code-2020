ids = []

# Unnecessary, used for visualizing.
grid = [[False for i in range(8)] for i in range(128)]


with open("input.txt") as file:
    data = [line for line in file]

for line in data:
    row = [0, 127]
    col = [0, 7]

    rdata = line[:7]
    cdata = line[7:-1]

    for i in rdata:
        diff = row[1] - row[0]
        if i == "F":
            row[1] -= diff // 2 + 1
        elif i == "B":
            row[0] += diff // 2 + 1

    for i in cdata:
        diff = col[1] - col[0]
        if i == "L":
            col[1] -= diff // 2 + 1
        elif i == "R":
            col[0] += diff // 2 + 1

    grid[row[0]][col[0]] = True
    ids.append(row[0] * 8 + col[0])

print("Seating grid:")
for num, i in enumerate(grid):
    print(num, ":", i)

for i in range(814):
    if i not in ids:
        if i - 1 in ids and i + 1 in ids:
            print("\nMy seat ID is {}".format(i))
