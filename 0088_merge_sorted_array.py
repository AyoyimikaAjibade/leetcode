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
# 1. Initialize three variables  
#  i. last = m + n - 1 for the last value of nums1
#  ii. n = n -1 for the last value of nums2
#  ii. m = m -1 for the last value of non-zero values of nums1
# 2. Iterate through the length of the nums1 until m and n is less than 0.
# 3. If the last value of nums1 i.e 'm' is greater than the last value of nums2 i.e 'n'
#  i. set nums1's last value i.e 'last' to 'm' value
#  ii. shift the last position to the left by decreasing it
#  iii. shift the 'm' position also to the left by decreasing it
# 4. If the last value of nums1 i.e 'm' is lesser than the last value of nums2 i.e 'n'
#  i. move the nums2 last value i.e 'n' to the last position i.e 'last' in nums1
#  ii. shift the last position to the left by decreasing it
#  iii. shift the 'n' position also to the left by decreasing it
# 5. if the n is not less than 0 meaning there are still more values in nums2 not in nums1, we copy the values of nums2 into nums1
# 4. Continue until the end of the array is reached.
# 5. Return nums1 values.

# time complexity = o(m + n)
# space complexity = o(n)

# def merge(nums1, m, nums2, n):
#     last = m + n - 1
#     while m > 0 and n > 0:
#         if nums1[m - 1] > nums2[n - 1]:
#             nums1[last] = nums1[m - 1]
#             m -= 1
#         else:
#             nums1[last] = nums2[n - 1]
#             n -= 1
#         last -= 1

#     # edge case: fill num1 with leftover from num2 elements
#     while n > 0:
#         nums1[last] = nums2[n - 1]
#         n = n - 1
#         last = last - 1
#     return nums1

def merge(nums1, m, nums2, n):
    l = m + n -1
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[l] = nums1[m-1]
            m -=1
        else:
            nums1[l] = nums2[n-1]
            n -=1
        l -= 1
    while n != 0:
        nums1[:l] = nums2[:n]
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