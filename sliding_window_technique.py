# template to solve most substring problems
# Sliding window algorithm is a problem solving technique that transforms two nested loops into one loop

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Steps to solve
def lengthOfLongestSubstring(char):
    # store the subarry in sets/current window
    charSet = set()
    left = 0
    result = 0

    for right in range(len(char)):
        # if the right character is alrrady in the current window
        while char[right] in charSet:
            # remove the left character
            charSet.remove(char[left])
            # and shift the left character forward
            left  +=1
        # else add the right character to the window
        charSet.add(char[right])
        # get the maximum length of the substring/windows
        result = max(result, right - left + 1)
    return result

str_char = 'abcabcbb'
str_char = 'bbbbb'
str_char = 'pwwkew'
print(lengthOfLongestSubstring(str_char))

