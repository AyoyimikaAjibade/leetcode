# Two pointer techniques for solving array problems

#27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Steps to solve:
# 1. Initialize the left_pointer to 0 which is to track the non_target element
# 2. Iterate through the length of the array.
# 3. Compare the current element with the target value. If they are different, move the current element to left_pointer position and increment 
# 4. Continue until the end of the array is reached.
# 5. Return left_pointer which represents the count of non-target elements.

# time complexity = o(n)
# space complexity = o(n)

def removeElement(nums, val):
    k = 0
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1 
    return k 

nums = [3,2,2,3], 
val = 3 #output 2, nums = [2,2,_,_]

nums = [0,1,2,2,3,0,4,2]
val = 2 #output 5, nums = [0,1,4,0,3,_,_,_]
print(removeElement(nums, val)) 