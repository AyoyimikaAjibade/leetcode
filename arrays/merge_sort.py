def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def main():
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    print("Sorted array is:", arr)

if __name__ == "__main__":
    main()


# O(n) linear space complexity, since it creates two additional arrays (left and right) to store the left and right 
# halves of the input during each recursive call. The memory required to store these arrays increases linearly 
# with the size of the input.
