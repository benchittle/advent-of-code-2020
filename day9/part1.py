import itertools

with open("input.txt") as file:
    data = list(map(int, file.read().split('\n')))


# Original solution
for start, num in enumerate(data[25:], 25):
    sums = set()
    for i in data[start - 25: start]:
        for j in data[start-25: start]:
            if i != j:
                sums.add(i + j)
    if num not in sums:
        break
print(num)


print("\n" + "#" * 10 + "\n")


# Solution using combinations
for endpos, num in enumerate(data[25:], 25):
    sums = map(sum, itertools.combinations(data[endpos - 25:endpos], 2))
    if num not in sums:
        break
print(num)