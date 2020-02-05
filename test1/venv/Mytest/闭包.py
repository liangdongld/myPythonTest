# 嵌套函数，且内部函数调用外部函数的变量
def outer():
    a = 10

    def inner():
        print(a)

    return inner


inn = outer()
inn()