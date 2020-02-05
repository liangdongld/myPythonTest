from urllib.request import urlopen


# 嵌套函数，且内部函数调用外部函数的变量
def outer():
    a = 10

    def inner():
        print(a)

    print(inner.__closure__)
    return inner


inn = outer()
inn()

ret = urlopen("https://www.jd.com/").read()
print(ret)
