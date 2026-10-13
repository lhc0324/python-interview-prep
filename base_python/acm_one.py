n = int(input())

nums = []
while len(nums) < n:
    parts = input().split()
    for p in parts:
        nums.append(int(p))

    nums.sort()

str_nums = []

for x in nums:
    s = str(x)
    str_nums.append(s)

res_str = " ".join(str_nums)

print(res_str)
