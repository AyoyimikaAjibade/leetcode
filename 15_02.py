# Algorithm

# 1. Count the frequency of each integer: Start by counting the frequency of each integer in the array. 
# This can be achieved by using a dictionary or a Counter.

# 2. Sort the frequencies of integers in ascending order. 
# This helps in determining which integers have the lowest frequency.

# 3. Iterate through the sorted frequencies, Always remove the integer with the lowest frequency first.
# and keeping track of items_removed 

# 4. if the items_removed is greater than k return the length of the sorted remaining unique frequency


from collections import Counter

def findLeastNumOfUniqueInts(arr, k):
    frequency_map = Counter(arr)
    
    sorted_frequencies = sorted(frequency_map.values())

    # track the number of items removed
    element_removed = 0

    for i in range(len(sorted_frequencies)):
        element_removed += sorted_frequencies[i]
        if element_removed > k:
            # If the number of elements removed exceeds k, return
            # the remaining number of unique elements
            return len(sorted_frequencies) - i
        
    # We have removed all elements, so no unique integers remain
    # Return 0 in this case
    return 0

# Example usage:
arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
# arr = [5, 5, 4]
# k = 1
print(findLeastNumOfUniqueInts(arr, k))  # Output: 2
