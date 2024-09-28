def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array is:", arr)

if __name__ == "__main__":
    main()

#  O(n²) quadratic time complexity, since the running time is quadratic in the size of the input. If the input size is n, 
# it will take approximately n² steps to complete the bubble sort.