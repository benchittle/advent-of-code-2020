import re, itertools, collections, math, numpy


# Original solution, janky as can be
with open("input.txt") as file:
    data = file.read().split("\n")

ids = list(map(int, data[1].replace("x,", "-1,").split(",")))
difs = []

buses = [i for i in ids if i != -1]
offsets = [i for i in range(len(ids)) if ids[i] != -1]

print(buses) #moduli
print(offsets) #remaindetrs

remainders = [0] + [busid - (offset % busid) for busid, offset in zip(buses, offsets)][1:]
print(remainders)


N = 1
for i in buses:
    N *= i

N_prods = []
for i in range(len(buses)):
    prod = 1
    for j in buses[:i] + buses[i + 1:]:
        prod *= j
    N_prods.append(prod)
print(N_prods)

x_vals = []
for n, busid in zip(N_prods, buses):
    #n = n % busid
    x = 1
    while True:
        if (n * x) % busid == 1:
            x_vals.append(x)
            break
        x += 1
print(x_vals)

time = sum([r * n * x for r, n, x in zip(remainders,N_prods, x_vals)]) % N
print(time)
