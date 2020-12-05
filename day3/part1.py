dxy_list = [(3, 1)]
length = 31

with open("input.txt") as file:
    data = list(file)

product = 1
for dx, dy in dxy_list:
    count = 0
    x = 0
    for line_num, line in enumerate(data):
        if line_num % dy == 0:
            if line[x % length] == "#":
                count += 1
            x += dx
    product *= count

print(product)
