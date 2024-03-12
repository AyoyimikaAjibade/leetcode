# Sliding window techniques for solving subarray problems

# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Steps to solve:
# 1. initailize the left and right pointer
# 2. initailize the max and current sum for comparison
# 3. increment the current sum with the array right pointer value
# 4. track the max sum while iterating
# 5. since the question did not state all array value are positive value,take care of the edge case
# 6. if the current sum is negative, decrease the current sum until it becomes non-negative
# 7. shift the left pointer forward and return the max subarray sum
def maxSubArray(arr_nums):
    # initialize the two pointers right and left
    left = 0
    # max_sum and current_sum to compare the greatest sum
    max_sum = float('-inf')
    current_sum = 0

    # expand the window by moving the right pointer to the right 
    for right in range(len(arr_nums)):
        # upon iteration add the right item to the current_sum
        current_sum += arr_nums[right]
        # check if the current sum is less than the max_sum
        # update the max_sum at every iteration
        max_sum = max(current_sum, max_sum)
        # since the question is not all positive value
        # current sum may becomes negative, we shrink the window by moving the left pointer 
        # to the right until the current sum becomes non-negative
        while current_sum < 0:
            current_sum -= arr_nums[left]
            left += 1
    return max_sum


nums = [1, -3, 2, 1, -1]
# nums = [-2,1,-3,4,-1,2,1,-5,4] # output = 6, subarray = [4,-1,2,1]
# nums = [1] # output = 1, subarray = [1]
# nums = [5,4,-1,7,8] # output = 23, subarray = [5,4,-1,7,8]
print(maxSubArray(nums))  # Output: 3 (Maximum sum subarray is [2, 1])