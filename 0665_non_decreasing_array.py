#665. Non-decreasing Array

# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# Steps to solve:
# 1. Initialize and keep track of any modifications by setting the 'modified' variable to False
# 2. Iterate through the array and skip if the next value i.e 'nums[i + 1]' is greater than the current value 'nums[i]'
# 3. Based on the task rules where we modify the value only once, if its already been changed return False immediately
# 4. For us to change the value in an increasing order we need to consider
#  i. if the next value i.e 'nums[i + 1]' is greater than the previous value 'nums[i - 1]' 
        # and we ensure we don't exceed the array index, change the current value to next value
#  ii. else if the above rule is false we change the next value to the current value and update the 'modified' variable to True
# 5. We return the lower case of the modified value in str

# time complexity = o(n)
# space complexity = o(1)

def checkPossibility(nums):
    modified = False

    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        if modified:
            return False
        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]
        modified = True
    return str(modified).lower()

nums = [4,2,3] #output true
# nums = [4,2,1] #output false
print(checkPossibility(nums)) 