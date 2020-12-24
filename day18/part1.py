import re

with open("input.txt") as file:
    expressions = file.read().split("\n")

def get_closing_bracket(expression, index):
    if expression[index] != "(":
        return None

    brackets = 1
    i = 1
    while brackets > 0:
        c = expression[index + i]
        if c == "(":
            brackets += 1
        elif c == ")":
            brackets -= 1
        i += 1

    return index + i - 1


def get_first_expression(expression):
    if expression[0] == "(":
        return get_closing_bracket(expression, 0)
    num = re.match(r"\d+", expression)
    if num is not None:
        return num.end() - 1


def expand(expression):
    i = 0
    expanded = []
    while i < len(expression):
        if expression[i] == "(":
            end = get_closing_bracket(expression, i)
            expanded.append(expand(expression[i + 1:end]))
            i = end + 1
        else:
            expanded.append(expression[i])
            i += 1
    exp = iter(expanded)
    num1 = int(next(exp))
    for op, num2 in zip(exp, exp):
        if op == "+":
            num1 += int(num2)
        elif op == "*":
            num1 *= int(num2)

    return num1

total = 0
for expression in expressions:
    total += expand(expression.replace(" ", ""))

print(total)


