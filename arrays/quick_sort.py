def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def main():
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()

# O(n * logn) quick sort time complexity. the time complexity is O(n²), if the pivot is always the smallest or largest element in the array.
# The time complexity of quick sort is determined by the number of recursive calls that are made. 
# Each recursive call processes approximately n/2 elements, so the total number of recursive calls is approximately log(n). 
# The running time of each recursive call is O(n), so the total running time is O(n * logn)

# O(logn) is a logarithmic space complexity. In the worst case, the space complexity is O(n), if the pivot is always the smallest or largest element in the array.
# This is because the call stack grows with the number of recursive calls, and the number of recursive calls is logarithmic in the size of the input.