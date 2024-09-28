# 1. Global Maximum
# Consider an array of distinct positive integers where the elements are sorted in ascending order.
# We want to find all the subsequences of the array consisting of exactly m elements. 
# For example, given array a = [1, 2, 3, 4], the subsequences consisting of m = 3 elements are [1, 2, 3], [1, 2, 4], [1, 3, 4], and [2, 3, 4]. 
# Once we have all of the m-element subsequences, we find the value of globalMaximum using the following pseudocode:

# globalMaximum = 0

# for each subsequence, s, consisting of m elements { 
#     currentMinimum = 1018
    
#     for each (x, y) pair of elements in subsequences { 
#         absoluteDifference = abs(x - y)
        
#         if absoluteDifference < currentMinimum (
#             currentMinimum absoluteDifference
#         )
#     )    
    
#     if currentMinimum > globalMaximum {

#         globalMaximum = currentMinimum
#     }
# }

# For example, given the array a = [2,3,5,9] and a length m = 3, first find all subsequences of length m.
# [2,3,5]
# [2,3,9]
# [2,5,9]
# [3,5,9]

# Debugging output from the pseudocode is:
# globalMaximum: 0
# Subsequence: [2, 3, 5]
# currentMinimum: 1000000000000000000
# x: 3 y: 2 abs (x-y): 1 currentMinimum: 1 
# x: 5 y: 2 abs (x-y): 3 currentMinimum: 1 
# x: 5 y: 3 abs (x-y): 2 currentMinimum: 1

def feas(a, m, diff):
    l = a[0]
    i = 0
    for _ in range(m - 1):
        while i < len(a) and a[i] < l + diff:
            i += 1
        if i == len(a):
            return False
        l = a[i]
    
    return True

def globalMaximum(a, m):
    i, j = 0, a[-1] - a[0]
    while i < j - 1:
        mid = (i + j) // 2
        
        if feas(a, m, mid):
            i = mid
        else:
            j = mid - 1
            
    return j if feas(a, m, j) else i

# Time complexity: O(N * log(X))