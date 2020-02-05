from functools import reduce
import math


def str2float(s):
    STR = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    s = s.split('.')

    def fun(x, y):
        return x * 10 + y

    def char2Num(s1):
        return STR[s1]

    x1 = reduce(fun, map(char2Num, s[0]))
    x2 = reduce(fun, map(char2Num, s[1]))
    x3 = x1 + x2 / math.pow(10, len(s[1]))
    return x3


print(str2float("123.333"))
l1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l1)
