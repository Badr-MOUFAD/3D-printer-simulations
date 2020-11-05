import numpy as np


# interval of the form [a, b]
# func is a function that returns true / false
# with propriety :
# func(a) == False --> for all x > a: func(x) == False
# func(a) == True --> for all x < a: func(x) == True
# objective is to narrow interval


def ContinuousBinarySearch(interval, func, precision_=10 ** -2, direction="negative"):
    a = interval[0]
    b = interval[1]
    precision = precision_

    if a == b:
        raise Exception("You need to provide an interval")

    if a > b:
        raise Exception("Verify that interval[0] < interval[1]")

    if direction == "negative":
        if func(a) and func(b):
            return a

        if (not func(a)) and (not func(b)):
            return b

        middle = (a + b) / 2

        if b - a < precision:
            return middle

        if func(middle):
            return ContinuousBinarySearch(interval=[a, middle], func=func, precision_=precision)
        else:
            return ContinuousBinarySearch(interval=[middle, b], func=func, precision_=precision)

    elif direction == "positive":
        if func(a) and func(b):
            return b
        if (not func(a)) and (not func(b)):
            return a

        middle = (a + b) / 2

        if b - a < precision:
            return middle

        if func(middle):
            return ContinuousBinarySearch(interval=[middle, b], func=func, precision_=precision, direction=direction)
        else:
            return ContinuousBinarySearch(interval=[a, middle], func=func, precision_=precision, direction=direction)



# input: func(starting) == True
def findSearchingInterval(starting, func, direction="positive"):
    length = 1

    if direction == "positive":
        while func(starting + length):
            length *= 2

        return [starting + int(length / 2), starting + length]
    else:
        while func(starting - length):
            length *= 2

        return [starting - length, starting - int(length / 2)]


# # example :
# def f(x):
#     if x < 5:
#         return True
#
#     return False
#
#
# interval = findSearchingInterval(0, func=f, direction="positive")
# print(interval)
# print(ContinuousBinarySearch(interval=interval, func=f, direction="positive"))
