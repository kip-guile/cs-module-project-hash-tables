# Your code here
import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


finals = {}
powers = {}
factorials = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x, y) in finals:
        return finals[(x, y)]
    else:
        if (x, y) in powers:
            power = powers[(x, y)]
        else:
            powers[(x, y)] = math.pow(x, y)
            power = powers[(x, y)]

        if power in factorials:
            factorial = factorial[power]
        else:
            factorials[power] = math.factorial(power)
            factorial = factorials[power]

        final = factorial // (x + y)
        final %= 982451653

        finals[(x, y)] = final
        return final


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(finals)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
