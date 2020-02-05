myInput = input()
myInput = myInput.split(" ")
tree = int(myInput[0])
student = int(myInput[1])
#Python中相除默认是加上小数点的，所以我们需要用int来转换不出小数点
print("%d %d" % (int(tree / student), int(tree % student)))