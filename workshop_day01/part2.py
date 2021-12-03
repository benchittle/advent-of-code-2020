from itertools import combinations

with open("input.txt") as file:
    intData = [int(n) for n in file.read().split()]

for triple in combinations(intData, 3):
    if sum(triple) == 2020:
        print(triple[0] * triple[1] * triple[2])
