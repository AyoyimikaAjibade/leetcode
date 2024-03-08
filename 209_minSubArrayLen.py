# Sliding window techniques for solving subarray problems

# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Steps to solve:
# 1. initailize the left and right pointer
# 2. initialize the sum of the total_window and length of the total window
# 3. increment the total_window with the right pointer value
# 4. keep track of the minimal length subarray encountered so far 
# 5. reduce the left pointer value from the total_window and shift the left pointer forward
# 6. return target_window_len if it has been updated and no longer infinity

def minSubArrayLen(target, nums):
    # keep track of the sum of the subarray items
    total_windows = 0
    left = 0
    # keep track of the length of the subarray items
    target_window_len = float('inf')

    for right in range(len(nums)):
        # sum up each value in the array until 
        # its greater than or equals to the target
        total_windows += nums[right]
        while total_windows >= target:
            # We keep track of the minimal length subarray encountered so far
            target_window_len = min(target_window_len, right - left + 1)
            # remove the left item from the sum of the subarray
            total_windows -= nums[left]
            # shift the left index forward
            left +=1
    #  return target_window_len if it has been updated and no longer infinity
    return target_window_len if target_window_len != float('inf') else 0

nums = [2,3,1,2,4,3]
target = 7
# nums = [5,1,3,5,10,7,4,9,2,8], target = 15, output = 2
# nums = [1,4,4], target = 4, output = 1
# nums = [1,1,1,1,1,1,1,1], target = 11, output = 0
print(minSubArrayLen(target, nums)) #output=2, subarray = [4,3]