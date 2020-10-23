# Will add comments and description later

import math


def solve(liters):
    res1 = liters / 24
    res2 = res1 - math.trunc(res1)
    if res2 != 0:
        res1 = res1 + 1
    return int(res1)


if __name__ == '__main__':
    x = float(input("Enter a number :"))
    print(solve(x))
