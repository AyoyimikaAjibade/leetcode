# Two pointer techniques for solving array problems

# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Steps to solve:
# 1. Initialize the left_pointer which is the next position to place a unique element in the array
# 2. Iterate through the array starting from the second element.
# 3. Compare the current element with the previous one. If they are different, move the current element to left_pointer position and increment 
# 4. Continue until the end of the array is reached.
# 5. Return left_pointer which represents the count of unique elements.

# time complexity = o(n)
# space complexity = o(n)
 
def removeDuplicates(nums):
        left_pointer = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[left_pointer] = nums[i]
                left_pointer +=1
        return left_pointer


nums = [1,1,2] #output 2, nums = [1,2,_]
nums = [0,0,1,1,1,2,2,3,3,4] #output 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(removeDuplicates(nums)) 