import math


def area_circle(r):
    return round(math.pi * (r**2), 2)


def hello_only():
    print('just say hello function')


def true_false(a, b):
    if a > b:
        return True
    else:
        print('a less than b. Test will be failed')

