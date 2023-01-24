# Este programa literalmente calcula usando funciones, no hay input sino solo las funciones

def zero(a=None):
    val = 0
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def one(a=None):
    val = 1
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def two(a=None):
    val = 2
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def three(a=None):
    val = 3
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def four(a=None):
    val = 4
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def five(a=None):
    val = 5
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def six(a=None):
    val = 6
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def seven(a=None):
    val = 7
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def eight(a=None):
    val = 8
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def nine(a=None):
    val = 9
    if a is None:
        return val
    else:
        if a[0] == '+':
            return val + a[1]
        elif a[0] == '-':
            return val - a[1]
        elif a[0] == '*':
            return val * a[1]
        elif a[0] == '/':
            return int(val / a[1])


def plus(n):
    return ['+', n]


def minus(n):
    return ['-', n]


def times(n):
    return ['*', n]


def divided_by(n):
    return ['/', n]


print(eight(divided_by(three())))
