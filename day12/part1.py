# Original solution
with open("input.txt") as file:
    data = file.read().split("\n")

vals = [(i[0], int(i[1:])) for i in data]

pos = [0, 0]
facing = 90

dirs = {0:"N", 90:"E", 180:"S", 270:"W"}

for d, val in vals:
    if d == "F":
        d = dirs[facing % 360]
    if d == "N":
        pos[1] += val
    elif d == "E":
        pos[0] += val
    elif d == "S":
        pos[1] -= val
    elif d == "W":
        pos[0] -= val
    elif d == "R":
        facing += val
    elif d== "L":
        facing -= val

print(abs(pos[0]) + abs(pos[1]))