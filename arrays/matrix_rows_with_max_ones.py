def findMaxOnesRow(mat):
    maxOnesIdx, maxOnesCount = 0, 0  # Initialize tracking variables
    for list_index, list_val in enumerate(mat):
        ones_count = sum(list_val)
        if ones_count > maxOnesCount:
            maxOnesIdx, maxOnesCount = list_index, ones_count
    return [maxOnesIdx, maxOnesCount] 

def main():
    arr = [[1, 0], [1, 1], [0, 1]]
    # arr = [[0, 1, 1], [0, 1, 1], [1, 1, 1]]
    # arr = [[1, 0, 1], [0, 0, 1], [1, 1, 0]]
    # arr = [[1, 1, 1, 1], [0, 0, 1], [1, 1, 0]]
    result = findMaxOnesRow(arr)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(m*n)
# space_complexity = O(1)