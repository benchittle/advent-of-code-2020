import re

def expand_rule(num, rules):
    rule = rules[num]
    if re.match(r'[a-zA-Z|]+$', rule) is not None:
        return rule

    rule = rule.split(" ")
    for i, subrule in enumerate(rule):
        if subrule.isnumeric():
            rule[i] =  expand_rule(int(subrule), rules)
    return "(" + "".join(rule) + ")"


with open("input.txt") as file:
    data = file.read().split("\n\n")

rules = {}
for line in data[0].split("\n"):
    num, rule = line.split(": ")
    rules[int(num)] = rule.replace('"', "")

count = 0
pattern = re.compile("^" + expand_rule(0, rules) + "$")
messages = data[1].split("\n")
for msg in messages:
    if re.match(pattern, msg) is not None:
        count += 1

print(count)
