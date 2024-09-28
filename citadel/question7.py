# Question 7: Minimum Operations to Reduce Array Elements to Zero


# Problem Statement:
# Given an array and two integers (x) and (y), in one operation, we can pick one element and subtract (x) from it, and subtract (y) from all other elements. The goal is to determine the minimum number of operations needed to reduce all elements of the array to zero.


# Approach: I employed a binary search approach to find the minimum number of operations efficiently.
# Time Complexity: O(NlogN)


def can_reduce_to_zero(arr, x, y, k):
    required_ops = 0
    for element in arr:
        if element <= k * y:
            continue
        extra_ops = (element - k * y + x - y - 1) // (x - y)
        required_ops += extra_ops
        if required_ops > k:
            return False
    return True

def min_operations_to_zero(arr, x, y):
    left, right = 0, max(arr) // min(x, y) + 1
    while left < right:
        mid = (left + right) // 2
        if can_reduce_to_zero(arr, x, y, mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example usage
arr = [10, 20, 30]
x, y = 3, 1
print(min_operations_to_zero(arr, x, y))