import re, copy

# Original solution
def display_space(space):
    for z, plane in enumerate(space):
        print(z)
        for y in plane:
            print(y)
        print()

def add_z_layers(space):
    y_size = len(space[0])
    x_size = len(space[0][0])

    plane = [list("." * x_size)] * y_size
    space.insert(0, plane.copy())
    space.append(plane.copy())

def add_y_rows(space):
    x_size = len(space[0][0])
    for zplane in space:
        row = list("." * x_size)
        zplane.insert(0, row)
        zplane.append(row)

def add_x_pads(space):
    for zplane in space:
        for y, yrow in enumerate(zplane):
            zplane[y] = ["."] + yrow + ["."]

def expand_space(space):
    add_x_pads(space)
    add_y_rows(space)
    add_z_layers(space)



def get_neighbours(space, pos, maxvals):
    xmax, ymax, zmax = maxvals
    x, y, z = pos
    n = []
    for zoff in range(-1, 2):
        #neighbours.append([])
        for yoff in range(-1, 2):
            #neighbours[zoff].append([])
            for xoff in range(-1, 2):
                #if (not (0 <= x + xoff < xmax)
                #and (0 <= y + yoff < ymax)
                #and (0 <= z + zoff < zmax)):
                #    neighbours.append(".")
                #else:
                n.append(space[z + zoff][y + yoff][x + xoff])
    assert len(n) == 27

    return n


with open("input.txt") as file:
    data = file.read()

space = [[list(s) for s in data.split("\n")]]
#print(space)
#display_space(space)
#quit()
add_z_layers(space)
expand_space(space)

for cycle in range(6):
    zmax = len(space)
    ymax = len(space[0])
    xmax = len(space[0][0])
    print("MAXES: ({}, {}, {})".format(xmax, ymax, zmax))

    expand_space(space)
    last_space = copy.deepcopy(space)

    print("\n===={}====\n".format(cycle))
    display_space(space)
    print("\n")

    for z in range(1, zmax + 1):
        for y in range(1, ymax + 1):
            for x in range(1, xmax + 1):
                current = last_space[z][y][x]
                neighbours = get_neighbours(last_space, (x, y, z), (xmax, ymax, zmax))
                if current == "#":
                    if not (2 <= neighbours.count("#") - 1 <= 3):
                        print("Off")
                        space[z][y][x] = "."
                else:
                    if neighbours.count("#") == 3:
                        print("on")
                        space[z][y][x] = "#"



#display_space(space)
count = 0
for z in space:
    for y in z:
        for x in y:
            count += x == "#"

print(count)