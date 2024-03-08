# Sliding window techniques for solving substring problems

# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring of s such that every character in t (including duplicates) is included 
# in the window. If there is no such substring, return the empty string ''

# Steps to solve:
# 1. use hashmpa to set the t_dict and s_dict to track the char frequency
# 2. edge case if t is an empty string return empty string
# 3. store the value and frequency of t characters in t_dict
# 4. initialize the left and right pointer as usual
# 5. initialize min_window and min_win_len to track te windos pointers and its length
# 6. initialize s_dict_len and t_dict_len for update and comparison
# 7. upon iteration create and update s_dict based on the right pointer value
# 8. if right pointer value in t_dict and s_dict right pointer value is same as t_dict right pointer value
# 9. increments the s_dict_lens for comparison to the t_dict_len
# 10. if t_dict_len and s_dict_len are equal while checking if the current window is the minimum
# 11. if the current window is less than the stored min_win_len
# 12. update the min_win value based on the current left and right pointer value
# 13. also update the min_win_len by the length of the left and right pointer value
# 14. if the current window length is greater than previous window length 
# 15. we shrink our window by decreasing the left value from the s_dict
# 16. if also the left pointer value was previously in the current window and the left 
# pointer value in the s_dict is lesser than the t_dict and decrease the s_dict_lens
# 17. otherwise shift the left pointer forward
# 18. since the min_wind contains the minumun string with the correct right and left pointer respectively
# 19. extraoplate and return the right and left pointer values from s respectively
def minWindow(s, t):
    if t == '':
        return ''

    t_dict, s_dict = {}, {}
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    
    left = 0
    min_win, min_win_len = [-1, -1], float('inf')
    s_dict_len, t_dict_len = 0, len(t_dict)

    for right in range(len(s)):
        right_val = s[right]
        s_dict[right_val] = s_dict.get(right_val, 0) + 1
        if right_val in t_dict and s_dict[right_val] == t_dict[right_val]:
            s_dict_len += 1
        while s_dict_len == t_dict_len:
            # update our min_win_len and return the min_win
            if(right - left + 1) < min_win_len:
                min_win = [left, right]
                min_win_len = right - left + 1
            # shrink our window by decreasing the left value from the s_dict
            # if the current window length is greater than previous window length
            left_val = s[left]  
            s_dict[left_val] -= 1
            if left_val in t_dict and s_dict[left_val] < t_dict[left_val]:
                s_dict_len -=1
            left += 1
    left, right = min_win
    #  return target_window_values if it has been updated and no longer infinity
    return s[left: right+1] if min_win_len != float('inf') else ''

# s = "ADOBECODEBANC"
# t = "ABC"
# s = "a", 
# t = "a" # Output= "a"
# s = "a", 
# t = "aa" # Output= ""
s = "ab"
t = 'b' # Output= b
print(minWindow(s, t)) #output BANC