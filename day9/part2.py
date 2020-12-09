import itertools
import pandas as pd

with open("input.txt") as file:
    data = list(map(int, file.read().split('\n')))

find = 26796446
max_length = len(data)


# Original solution
for group_size in range(2, max_length):
    for i in range(max_length - group_size):
        if sum(data[i:i+group_size]) == find:
            print(min(data[i:i+group_size]) + max(data[i:i+group_size]))
            break

'''
# Solution using combinations
for group_size in range(2, max_length):
    for group in map(sum, itertools.combinations(data, group_size)):
        if sum(group) == find:
            print(max(group) + min(group))
            break
'''

ser = pd.Series(data)
print(ser)

for group_size in range(2, max_length):
    print(ser[ser.rolling(group_size).sum() == find])