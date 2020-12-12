import math

pos = [0, 0]
waypoint = [10, 1]


# Original solution
def rotate(vec, deg):
    if deg == 90:
        vec[0], vec[1] = vec[1], -vec[0]
    elif deg == 180:
        vec[0] *= -1
        vec[1] *= -1
    elif deg == 270:
        vec[0], vec[1] = -vec[1], vec[0]


with open("input.txt") as file:
    data = file.read().split("\n")

vals = [(i[0], int(i[1:])) for i in data]
for d, val in vals:
    if d == "F":
        for i in range(val):
            pos[0] += waypoint[0]
            pos[1] += waypoint[1]

    if d == "N":
        waypoint[1] += val
    elif d == "E":
        waypoint[0] += val
    elif d == "S":
        waypoint[1] -= val
    elif d == "W":
        waypoint[0] -= val
    elif d == "R":
        rotate(waypoint, val)
    elif d== "L":
        rotate(waypoint, (360 - val) % 360)

print(abs(pos[0]) + abs(pos[1]))



# Slightly more general solution
def rotateccw(vec, deg):
    rad = math.radians(deg)
    s = math.hypot(vec[0], vec[1])
    x = vec[0]
    y = vec[1]
    vec[0] = x * math.cos(rad) - y * math.sin(rad)
    vec[1] = x * math.sin(rad) + y * math.cos(rad)


with open("input.txt") as file:
    data = file.read().split("\n")

movements = [(i[0], int(i[1:])) for i in data]

pos = [0, 0]
waypoint = [10, 1]

for direction, value in vals:
    if direction == "F":
        pos[0] += waypoint[0] * value
        pos[1] += waypoint[1] * value

    if direction == "N":
        waypoint[1] += value
    elif direction == "E":
        waypoint[0] += value
    elif direction == "S":
        waypoint[1] -= value
    elif direction == "W":
        waypoint[0] -= value
    elif direction == "R":
        rotateccw(waypoint, -value)
    elif direction == "L":
        rotateccw(waypoint, value)

print(abs(pos[0]) + abs(pos[1]))