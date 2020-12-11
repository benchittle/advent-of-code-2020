import re
import pandas as pd

def get_neighbours(data, row, col):
    neighbours = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            try:
                r = row + i - 1
                c = col + j - 1
                if r < 0 or c < 0:
                    raise IndexError
                neighbours[i][j] = data[r][c]
            except IndexError:
                neighbours[i][j] = "."
    return neighbours


with open("input.txt") as file:
    data = file.read().split("\n")

data = [list(i) for i in data]

rows = len(data)
cols = len(data[0])

current = data[:]
last = []
while current != last:
    last = [i[:] for i in current]
    current = [i[:] for i in last]


    for row in range(rows):
        for col in range(cols):
            adj = "".join(["".join(i) for i in get_neighbours(last, row, col)])
            #print(adj)
            #print()

            if adj[4] == "L" and re.match(r"[L.]{9}", adj) is not None:
                current[row][col] = "#"
            elif adj[4] == "#" and adj.count("#") - 1 >= 5:
                current[row][col] = "L"

print("".join(["".join(i) for i in current]).count("#"))



