# Two pointers techniques a general version of the sliding window techniques for solving substring problems

# 647. Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.

# Steps to solve:
# 1. initialize the count for each palidromic substring
# 2. for odd index position, we set left and right pointer 
# to the current index while looping through the string
# 3. for even index position, we set left pointer to the current index 
# and right pointer to the current index plus one while looping through the string
# 4. for the odd index position, if the right and left value are the same and the left is greater than 
# or equals to zero and the right pointer is less than the length of the string we;
# 5. we increment the count for each palindromic substring, move the left pointer backwards and the right pointer forward
# 6, finally, we return the number of palindromic substring

def countSubstrings(strs):
    num_pal_sub = 0

    for index in range(len(strs)):
        # odd indexes
        num_pal_sub += count_palidrom(strs, index, index)
        # even indexes
        num_pal_sub += count_palidrom(strs, index, index+1)

    return num_pal_sub

def count_palidrom(strs, lef, rig):
    res = 0
    while lef>= 0 and rig < len(strs) and strs[rig] == strs[lef]:
            res += 1
            lef -= 1
            rig +=1
    return res 

strs = "abc" #Output: 3
# strs = "aaa" #output: 6
print(countSubstrings(strs))