myInput = list(map(lambda x: int(x), input().split(" ")))
sum = myInput[0]
for i in range(0, int((myInput[1] - myInput[0]) / myInput[2])):
    myInput[0] = myInput[0] + myInput[2]
    sum = sum + myInput[0]
print(sum)