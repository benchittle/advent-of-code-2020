import re

with open("input.txt") as file:
    data = file.read().split("\n")

tiles = {}


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
print(tiles)
print(len(tiles))
print(list(tiles.values()).count(-1))
