myInput = input().split(" ")
nums = []
for i in range(0,3):
    nums.append(int(myInput[i]))
    print("%-9d%-9d%-9d" %(nums[i],nums[i]**2,nums[i]**3))