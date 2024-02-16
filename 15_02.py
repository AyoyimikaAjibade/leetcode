# Algorithm

# 1. Count the frequency of each integer: Start by counting the frequency of each integer in the array. 
# This can be achieved by using a dictionary or a Counter.

# 2. Sort the frequencies of integers in ascending order. 
# This helps in determining which integers have the lowest frequency.

# 3. Iterate through the sorted frequencies, removing elements until k becomes 0. 
# Always remove the integer with the lowest frequency first.

# 4. Count the unique integers left after removing k elements.


from collections import Counter

def findLeastNumOfUniqueInts(arr, k):
    # Step 1: Count the frequency of each integer
    frequency_map = Counter(arr)
    
    # Step 2: Sort the frequencies
    sorted_frequencies = sorted(frequency_map.values())
    
    # Step 3: Remove elements until k becomes 0
    for freq in sorted_frequencies:
        if k >= freq:
            # If we have enough remaining removals to completely remove this frequency,
            # subtract this frequency from k
            k -= freq
            # If the frequency is completely removed, it doesn't contribute to the unique integers left
            frequency_map.pop(freq, None)
        else:
            # If we don't have enough remaining removals to completely remove this frequency,
            # stop the loop
            break
    
    # Step 4: Count unique integers left
    return len(frequency_map)

# Example usage:
arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
print(findLeastNumOfUniqueInts(arr, k)) 