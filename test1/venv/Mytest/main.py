num = 100
while num < 1000:
    a = int(num / 100)
    b = int(num / 10 % 10)
    c = int(num % 10)
    sum = a ** 3 + b ** 3 + c ** 3
    if sum == num:
        print(sum)
    num = num + 1