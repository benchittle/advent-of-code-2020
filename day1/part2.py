import itertools

with open("input.txt") as file:
    nums = [int(line[:-1]) for line in file]

for i in itertools.combinations(nums, 3):
    if sum(i) == 2020:
        print(i[0] * i[1] * i[2])