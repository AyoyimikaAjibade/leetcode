# Two pointers techniques a general version of the sliding window techniques for solving substring problems

# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
# objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Steps to solve:
# 1. initialize left to 0, right to the last index and indexe pointer
#  to 0 for every time it loop through the array
# 2. going through the array when the indexe is less than the last array index
# 3. if the current index val is equals to 0, swap the value to the left and move the left pointer forward
# 4. if the current index val is equals to 2, swap the value to the right and move the right pointer backward
# 5. as an edge case, swapping a 2 should not move the indexe pointer forward so we decreament
# 6. increase the index pointer if the array value is not 0 or 2

def sortColors(arr_nums):
    left, right, indexe = 0, len(arr_nums) - 1, 0

    def swap(indexe, pos):
        tmp = arr_numbers[indexe]
        arr_nums[indexe] = arr_numbers[pos]
        arr_nums[pos] = tmp

    while indexe <= right:
        if arr_nums[indexe] == 0:
            swap(left, indexe)
            left += 1
        elif arr_nums[indexe] == 2:
            swap(indexe, right)
            right -= 1
            indexe -= 1
        indexe += 1
    return arr_nums

# arr_numbers = [2,0,2,1,1,0]
arr_numbers = [2,0,1] #output: [0,1,2]
print(sortColors(arr_numbers)) # Output: [0,0,1,1,2,2]