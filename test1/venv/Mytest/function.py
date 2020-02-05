from functools import reduce


def f(x, y):
    return x * y


def g(x):
    return x ** 2


def tran(name):
    return str.upper(name[0]) + str.lower(name[1:])


def pord(lis):
    return reduce(lambda x, y: x * y, lis)


l1 = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(f, l1)
print(r)
q = map(g, l1)
print(list(q))
a = ["asdfSSDa", "adsfSSS", "gSSasdfas"]
print(list(map(tran, a)))
print(pord([1, 2, 3, 4]))
