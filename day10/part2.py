from collections import Counter
import itertools

with open("input.txt") as file:
    data = sorted(map(int, file.read().split("\n")))

rating = data[-1] + 3

data = [0] + data + [rating]

count = 0

# Original Solution

difs = [j - i for i, j in zip(data[:-1], data[1:])]
'''
i = 0
dif_lengths = [0]
for d in difs:
    if d == 1:
        dif_lengths[i] += 1
    else:
        i += 1
        dif_lengths.append(0)
dif_len_counts = Counter(dif_lengths)


combos = 7 ** dif_len_counts[4] * 4 ** dif_len_counts[3] * 2 ** dif_len_counts[2]
print(combos)

'''


def get_mods(difs):
    mods = []
    for i in range(len(difs) - 1):
        new = difs[:]
        new[i] = new[i + 1] + new.pop(i)
        mods.append(new + get_mods(new))
    return mods

# Consecutive differences between the adapters.
difs = [j - i for i, j in zip(data[:-1], data[1:])]

groups = Counter(" ".join(map(str, difs)).split("3"))
groups.pop(" ")
groups.pop("")

for group in groups:
    nums = list(map(int, group.strip().split(" ")))
    print(get_mods(nums))


print(groups)




