from math import sqrt


# filter函数
# 水仙花数
def solution(x):
    a = int(x / 100)
    b = int(x / 10 % 10)
    c = int(x % 10)

    # print("a = %d  b = %d  c = %d" % (a, b, c))
    # print("a = %d  b = %d  c = %d" % (a ** 3, b ** 3, c ** 3))
    return (a ** 3) + b ** 3 + c ** 3 == x


# 过滤掉所有非字符串
def is_str(x):
    return type(x) == str


# x开平方是否为整数
def is_int(x):
    return sqrt(x) % 1 == 0


ret = filter(solution, [i for i in range(100, 1000)])
for i in ret:
    print(i)
ret = filter(is_str, [1, 2, 3, 4, "dfasdf", "dfad"])
for i in ret:
    print(i)
ret = filter(is_int, [i for i in range(1, 101)])
for i in ret:
    print(i)
