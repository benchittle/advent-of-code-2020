import re

with open("input.txt") as file:
    data = file.read().split("\n")

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


def get_opening_bracket(expression, index):
    if expression[index] != ")":
        return None

    brackets = 1
    i = 1
    while brackets > 0:
        c = expression[index - i]
        if c == ")":
            brackets += 1
        elif c == "(":
            brackets -= 1
        i += 1

    return index - i + 1


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


def add_brackets_addition(expression):
    expression = list(expression)
    i = 0
    while i < len(expression):
        if expression[i] == "+":
            if expression[i + 1] == "(":
                expression.insert(get_closing_bracket(expression, i + 1), ")")
            else:
                expression.insert(i + 2, ")")

            if expression[i - 1] == ")":
                expression.insert(get_opening_bracket(expression, i - 1), "(")
            else:
                expression.insert(i - 1, "(")
            i += 1
        i += 1
    return "".join(expression)


expressions = [add_brackets_addition(line.replace(" ", "")) for line in data]

total = 0
for expression in expressions:
    total += expand(expression)

print(total)


