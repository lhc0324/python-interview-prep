#二分查找

def binary_search(nums,target):
  left = 0,right = len(nums) - 1
  while left <= right:
    mid = left + (right - left)//2
    if mid == target:
      return mid
    elif mid < target:
      left = mid + 1 
    elif mid > target:
      right = mid - 1
  return -1