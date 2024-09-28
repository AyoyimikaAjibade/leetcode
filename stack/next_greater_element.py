def nextLargerElement(arr):
    # Initialize an empty stack and a result list with -1 values
    s = []
    res = [-1] * len(arr)

    # Iterate through the array in reverse order
    for i in range(len(arr) - 1, -1, -1):
        # While the stack is not empty and the top element of the stack is less than or equal to the current element
        while s and s[-1] <= arr[i]:
            s.pop()  # Pop elements from the stack until the condition is met
        
        if s: 
            res[i] = s[-1]  # If the stack is not empty, set the result for the current element to the top element of the stack
        s.append(arr[i])  # Push the current element onto the stack

    return res


def main():
    arr = [4, 5, 2, 25]
    arr = [13, 7, 6, 12]
    # arr = [1, 2, 3, 4, 5]
    result = nextLargerElement(arr)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)