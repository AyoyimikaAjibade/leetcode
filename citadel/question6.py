# Question 6: Subarray with a Specific Property


# Problem Statement:
# Given an array of length (10^5), we had to find the number of subarrays that satisfied the condition:
# arr[i] == arr[j] == sum(arr[i+1 : j-1])
# where (i) and (j) are indices of the array.


# To solve this problem, I used a prefix array combined with hashing.


def q1(arr):
    # dp[el][s] = num times we have a prefix of s, with element
    # "el" right after it
    # to solve the problem, for each a[i], we find how many
    # dp[a[i]][3*a[i]] we have for it
    n = len(arr)
    ret = s = 0
    dp = {arr[0]: {0: 1}}
    for i,el in enumerate(arr):
        s += el
        if el not in dp:
            dp[el] = {}
        dpSub = dp[el]
        want = 3*el
        ret += dpSub.get(s - want, 0)
        if i != n-1:
            nxt = arr[i+1]
            if nxt not in dp:
                dp[nxt] = {}
            dp[nxt][s] = dp[nxt].get(s, 0) + 1

    return ret