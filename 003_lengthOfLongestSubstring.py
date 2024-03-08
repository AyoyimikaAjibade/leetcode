# Sliding window techniques for solving substring problems

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Steps to solve:
# 1. initailize curr_wind variable in a set as this data type is suitable for non-duplicate characters
# 2. initailize the pointers; left = 0 and right is each index in the character while looping
# 3. initailize the uniques substring character as result
# 4. Expand the window by moving the right pointer to the right and updating the window state.
# 5. looping through the char check if the right char is in the current sliding window
# 6. if right char is present in the current sliding window; remove the char from the current sliding window
# and shift the left pointer forward
# 7. repeat step 5, 6 until the end of the string
# 8. if right char is not present in the current sliding window add it to the current window
# 9. to get the length of the unique longest substring use the max() to compare the current window length
def lengthOfLongestSubstring(char):
    # store the substr in sets/current window
    curr_win = set()
    left = 0
    result = 0

    for right in range(len(char)):
        # if the right character is already in the current window
        while char[right] in curr_win:
            # remove the left character
            curr_win.remove(char[left])
            # and shift the left character forward
            left  +=1
        # else add the right character to the window
        curr_win.add(char[right])
        # keep track of the maximum length of the substring/windows
        result = max(result, right - left + 1)
    return result

# str_char = 'abcabcbb' # output = 3, window = 'abc
# str_char = 'bbbbb' # output = 1, window = 'b'
str_char = 'pwwkew' # output = 3, window = 'wke'
print(lengthOfLongestSubstring(str_char))