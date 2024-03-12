# Sorting the array techniques a general version of the sliding window techniques 
# for solving substring problems

# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all 
# overlapping intervals, and return an array of the non-overlapping intervals 
# that cover all the intervals in the input.

# Steps to solve:
# 1. 

def merge(intervals):
    intervals.sort(key = lambda i: i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])
    return output

intervals = [[1,3],[2,6],[8,10],[15,18]] #0utput: [[1,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]] #output: [[1,5]]
print(merge(intervals))