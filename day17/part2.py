import copy

def display(space):
    for w, wspace in enumerate(space):
        print("\n\n=={}==".format(w))
        for z, zspace in enumerate(wspace):
            print("\n--{}--".format(z))
            for y in zspace:
                print(y)

def expand_x(space):
    for w in space:
        for z in w:
            for y in z:
                y.insert(0, ".")
                y.append(".")

def expand_y(space):
    xsize = len(space[0][0][0])
    for w in space:
        for z in w:
            z.insert(0, ["." for i in range(xsize)])
            z.append(["." for i in range(xsize)])

def expand_z(space):
    xsize = len(space[0][0][0])
    ysize = len(space[0][0])
    for w in space:
        w.insert(0, [["." for i in range(xsize)] for j in range(ysize)])
        w.append([["." for i in range(xsize)] for j in range(ysize)])

def expand_w(space):
    xsize = len(space[0][0][0])
    ysize = len(space[0][0])
    zsize = len(space[0])
    space.insert(0, [[["." for i in range(xsize)] for j in range(ysize)] for k in range(zsize)])
    space.append([[["." for i in range(xsize)] for j in range(ysize)] for k in range(zsize)])

def expand_space(space):
    expand_x(space)
    expand_y(space)
    expand_z(space)
    expand_w(space)


def get_neighbours(space, pos):
    x, y, z, w= pos
    n = []
    for woff in range(-1, 2):
        for zoff in range(-1, 2):
            for yoff in range(-1, 2):
                for xoff in range(-1, 2):
                    n.append(space[w + woff][z + zoff][y + yoff][x + xoff])
    return n


with open("input.txt") as file:
    data = file.read()

space = [[[list(s) for s in data.split("\n")]]]
expand_space(space)

for cycle in range(6):
    wmax = len(space)
    zmax = len(space[0])
    ymax = len(space[0][0])
    xmax = len(space[0][0][0])

    expand_space(space)
    last_space = copy.deepcopy(space)

    for w in range(1, wmax + 1):
        for z in range(1, zmax + 1):
            for y in range(1, ymax + 1):
                for x in range(1, xmax + 1):
                    current = last_space[w][z][y][x]
                    neighbours = get_neighbours(last_space, (x, y, z, w))
                    if current == "#":
                        if not (2 <= neighbours.count("#") - 1 <= 3):
                            space[w][z][y][x] = "."
                    else:
                        if neighbours.count("#") == 3:
                            space[w][z][y][x] = "#"

count = 0
for w in space:
    for z in w:
        for y in z:
            for x in y:
                count += x == "#"

print(count)
