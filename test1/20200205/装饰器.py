# 在不修改函数执行方式的情况下，继续为函数添加功能
import time


def timer(f):  # 装饰器函数
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(0.1)
        inner_ret = f(*args, **kwargs)  # 被装饰的函数
        print(time.time() - start)
        return inner_ret

    return inner


@timer  # 语法糖 @装饰器函数名
def func(x):  # 被装饰的函数
    print('ddd', x)
    return True

@timer
def func1(x, y, z):
    print(x, y, z)
    return x


# func = timer(func)
ret = func1(11, 12, 13)
print(ret)
