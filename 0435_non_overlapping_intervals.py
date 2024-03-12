# Sorting the array techniques a general version of the sliding window techniques 
# for solving substring problems

# 435. Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest 
# of the intervals non-overlapping.

# Steps to solve:
# 1. 

def eraseOverlapIntervals(intervals):
    intervals.sort()
    result = 0
    previous_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= previous_end:
            previous_end = end
        else:
            result += 1
            previous_end = min(end, previous_end)
    return result

intervals = [[1,2],[2,3],[3,4],[1,3]] #output: 1
# intervals = [[1,2],[1,2],[1,2]] output: 2
# intervals = [[1,2],[2,3]] #output: 0
print(eraseOverlapIntervals(intervals))