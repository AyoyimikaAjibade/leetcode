# Two pointer techniques for solving array problems

#1929. Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where 
# ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Steps to solve:
# 1. Initialize the result array with zero elements of the doubled length of the input value
# 2. Iterate through the length of the array.
# 3. Fill the result array with the items values i.e result_arr[index] = input_value[index] (first half).
# 4. Fill the result array with the items values starting from the length of the original array i.e result_arr[index + len(input_value)] = input_value[index].
# 5. Return result array.

# time complexity = o(n^2)
# space complexity = o(n^2)

def getConcatenation(nums):
    len_nums = len(nums)
    ans = [0] * len_nums * 2
    for num in range(len_nums):
        ans[num] = nums[num]
        ans[num + len_nums] = nums[num]

    return ans

nums = [1,2,1] #output [1,2,1,1,2,1]
nums = [1,3,2,1] #output [1,3,2,1,1,3,2,1]
print(getConcatenation(nums)) 