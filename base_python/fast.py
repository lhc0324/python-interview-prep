#快速排序

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums)//2]
    left = []
    mid = []
    right = []
    for x in nums:
        if x < pivot:
            left.append(x)
        if x == pivot:
            mid.append(x)
        if x > pivot:
            right.append(x)
    return quick_sort(left) + quick_sort(mid) + quick_sort(right)

if __name__ == "__main__" :
    nums = [5,2,9,1,7,3]
    sorted_nums = quick_sort(nums)
    print(sorted_nums)
    