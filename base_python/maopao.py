#冒泡排序

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False 
        for j in range(0,n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j + 1] = nums[j + 1],nums[j]
                swapped = True
        if not swapped:
            break
    return nums


if __name__ == "__main__":
    nums = [5,2,9,1,7,3] 
    bubble_nums = bubble_sort(nums)
    print(bubble_nums)