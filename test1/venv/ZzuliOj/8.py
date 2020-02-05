nums = list(map(lambda x: int(x), input().split(" ")))
n = (nums[0] * 4 - nums[1]) / 2
m = nums[0] - n
print("%d %d" % (n, m))
