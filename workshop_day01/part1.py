
""" file = open("sample.txt")

print(file.read())

file.close() """

with open("input.txt") as file:
    data = file.read()

intData = []
for n in data.split("\n"):
    intData.append(int(n))

for i in range(len(intData)):
    for j in range(i + 1, len(intData)):
        if intData[i] + intData[j] == 2020:
            print(intData[i] * intData[j])

