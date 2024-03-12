# Two pointers techniques a general version of the sliding window techniques for solving substring problems

# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored 
# inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m 
# elements denote the elements that should be merged, and the last n elements are set to 0 and should 
# be ignored. nums2 has a length of n.

# Steps to solve:
# 1. initialize the last index based of the length of m and n
# 2. whil the length of nums1 and nums2 is less than 0 respectively
# 3. if the value of nums1 is greater than nums2, then set the last value of num1 to num1
# 4. if the value of num1 is lesser than or equals num2 set the last value of num1 to num2
#5. edge case: if there is a remaining value in num2 fill the leftover in num1 remaining space

def merge(nums1, m, nums2, n):
    last = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    # edge case: fill num1 with leftover from num2 elements
    while n > 0:
        nums1[last] = nums2[n - 1]
        n = n - 1
        last = last - 1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3 #output: [1,2,2,3,5,6]
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0 #output: [1]
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1 #output: [1]
print(merge(nums1, m, nums2, n))