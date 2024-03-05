# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
# While moving from building i to building i+1 (0-indexed),

# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

import heapq

def furthestBuilding(heights, bricks, ladders):
    diff_heap = []  # Priority queue to store differences in heights
    n = len(heights)
    
    for i in range(n - 1):
        diff = heights[i + 1] - heights[i]  # Calculate height difference
        if diff > 0:
            heapq.heappush(diff_heap, diff)  # Push positive differences into the heap
            print('diff_heap', diff_heap)
            if len(diff_heap) > ladders:  # If we have more differences than available ladders
                bricks -= heapq.heappop(diff_heap)  # Use bricks to cover the difference
                print('bricks', bricks)
                if bricks < 0:  # If we run out of bricks
                    return i  # Return the index of the last reached building
    return n - 1  # If we reach the end, return the index of the last building

# heights = [4,2,7,6,9,14,12]
# bricks = 5
# ladders = 1
heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
# heights = [14,3,19,3]
# bricks = 17
# ladders = 0

answer = furthestBuilding(heights, bricks, ladders)
print(answer)