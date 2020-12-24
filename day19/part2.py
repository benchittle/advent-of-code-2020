import re

def expand_rule(num, rules):
    rule = rules[num]
    if re.match(r'[a-zA-Z|+]+$', rule) is not None:
        return rule

    rule = rule.split(" ")
    for i, subrule in enumerate(rule):
        if subrule.isnumeric():
            #if subrule in visited:
                #return '+'
            #else:
            rule[i] =  expand_rule(int(subrule), rules)
            #visited.add(subrule)
    return "(" + "".join(rule) + ")"



with open("input.txt") as file:
    data = file.read().split("\n\n")

rules = {}
for line in data[0].split("\n"):
    num, rule = line.split(": ")
    rules[int(num)] = rule.replace('"', "")


rules[8] = "{}+".format(expand_rule(42, rules))

# lol I can't be bothered how to make
# "{}+{}+",format(expand_rule(42, rules), expand_rule(31, rules))
# match the same amount of the second + as the first + so that's how we got here
rules[11] = ('42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 '
 '42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 '
 '42 42 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 '
 '| 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 '
 '42 42 42 42 31 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 42 42 '
 '31 31 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 42 42 42 31 31 '
 '31 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 42 42 42 42 31 31 '
 '31 31 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 42 42 42 42 42 '
 '31 31 31 31 31 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 42 42 '
 '42 42 42 42 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 '
 '42 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 '
 '31 | 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 '
 '31 31 31 31 31 31 31 31 31 31')

count = 0
pattern = re.compile("^" + expand_rule(0, rules) + "$")

messages = data[1].split("\n")
for msg in messages:
    if re.match(pattern, msg) is not None:
        count += 1

print(count)

s1 = ""
s2 = ""
s = ""
for i in range(60):
    s1 += "a"
    s2 += "b"
    s += s1 + s2 + "|"