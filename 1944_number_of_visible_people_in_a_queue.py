# Traversing from the right techniques a general version of the sliding window techniques 
# for solving substring problems

# 1944. Number of Visible People in a Queue
# There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order.
# You are given an array heights of distinct integers where heights[i] represents the height of the ith person.
# A person can see another person to their right in the queue if everybody in between is shorter than 
# both of them. More formally, the ith person can see the jth person 
# if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).
# Return an array answer of length n where answer[i] is the number of people the ith
# person can see to their right in the queue.

# Steps to solve:
# 1. 

def canSeePersonsCount(heights):
    pass

heights = [10,6,8,5,11,9] #Output: [3,1,2,1,1,0]
# heights = [5,1,2,3,10] 0utput: [4,1,1,1,0]
print(canSeePersonsCount(heights))