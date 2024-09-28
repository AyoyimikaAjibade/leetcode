#189. Rotate Array

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Steps to solve:
# 1. Initialize the length of the array and also handles edge cases where 'k' is greater than 'n'
# 2. Temporarily and move all the elements of the array based on the 'k' value but in reverse order
# 3. Reverse the first 'k' elements to put them in the correct order
# 4. Reverse the elements from position 'k' to the end of the array to place them in the correct order

# time complexity = o(n)
# space complexity = o(1)

def rotateArray(nums, k):
    n = len(nums)
    k = k % n #handles edge cases where 'k' is greater than 'n'

    #helper function to reverse sections of the array
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
    #reverse the entire array
    reverse(0, n - 1)
    #reverse the k section of the array
    reverse(0, k - 1)
    #reverse the remaining section of the array
    reverse(k, n - 1)

    return nums

nums = [1,2,3,4,5,6,7] 
k = 3 #output [5,6,7,1,2,3,4]
nums = [-1,-100,3,99]
k = 2 #output [3,99,-1,-100]
print(rotateArray(nums, k)) 