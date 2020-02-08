# 默写装饰器模式
def solution(func):
    def inner(*args, **kwargs):
        # 待添加内容
        ret = func(*args, **kwargs)
        # 待添加内容
        return ret

    return inner


@solution  # func1 = solution(func1)
def func1(x):
    a = int(x / 100)
    b = int(x / 10 % 10)
    c = int(x % 10)
    if a ** 3 + b ** 3 + c ** 3 == x:
        return x
    return 0


for i in range(100, 1000):
    if func1(i) != 0:
        print(func1(i))
