import copy

def get_neighbours(pos, tiles_copy, tiles):
    # Return the 6 neighbours around the specified tile. 
    neighbours = []
    offsets = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
    for rowoff, coloff in offsets:
        neighbourpos = (pos[0] + rowoff, pos[1] + coloff)
        if neighbourpos in tiles_copy:
            neighbours.append(tiles_copy[neighbourpos])
        else:
            #Adds out of bounds tiles to the grid so they'll be considered the next day.
            tiles[neighbourpos] = 1
            neighbours.append(1)
    return neighbours


def fill_grid(tiles):
    coords = list(tiles.keys())
    minrow = min(coords)[0]
    mincol = min(coords, key=lambda x: x[1])[1]
    maxrow = max(coords)[0]
    maxcol = max(coords, key=lambda x: x[1])[1]

    for row in range(minrow, maxrow + 1):
        for col in range(mincol, maxcol + 1):
            pos = (row, col)
            if pos not in tiles:
                tiles[pos] = 1
    

with open("input.txt") as file:
    data = file.read().split("\n")

tiles = {}

#day 1 stuff
for directions in data:
    pos = [0, 0]
    directions = directions.replace("se", "h").replace("sw", "g").replace("ne", "y").replace("nw", "t")
    for d in directions:
        if d == "e":
            pos[1] += 1
        elif d == "w":
            pos[1] -= 1
        elif d == "y":
            pos[0] += 1
        elif d == "t":
            pos[0] += 1
            pos[1] -= 1
        elif d == "g":
            pos[0] -= 1
        elif d == "h":
            pos[0] -= 1
            pos[1] += 1
    pos = tuple(pos)
    if pos in tiles:
        tiles[pos] *= -1
    else:
        tiles[pos] = -1

print(list(tiles.values()).count(-1))
print()

#day 2 stuff

# Place white tiles just past the extremes so that one layer of white tiles will
# be padded on all sides when the grid is filled in.
minrow = min(tiles.keys())[0]
mincol = min(tiles.keys(), key=lambda x: x[1])[1]
maxrow = max(tiles.keys())[0]
maxcol = max(tiles.keys(), key=lambda x: x[1])[1]
tiles[(maxrow + 1, mincol - 1)] = 1
tiles[(minrow - 1, maxcol + 1)] = 1

# Fill any holes in the grid with white tiles.
fill_grid(tiles)


for day in range(100):
    prev_tiles = copy.deepcopy(tiles)
    for pos in prev_tiles:
        neighbours = get_neighbours(pos, prev_tiles, tiles)
        current = tiles[pos]
        blacks = neighbours.count(-1)

        if current == -1 and (blacks == 0 or blacks > 2):
            tiles[pos] *= -1
        elif current == 1 and (blacks == 2):
            tiles[pos] *= -1

    print(list(tiles.values()).count(-1))
