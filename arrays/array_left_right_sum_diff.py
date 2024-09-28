# def findDifferenceArray(nums):
#     n = len(nums)
#     differenceArray = [0] * n
#     left_array = []
#     for i in range(n):
#         if i != 0:
#             left_array = nums[:i]
#         differenceArray[i] = abs(sum(left_array) - sum(nums[i + 1:]))
#     return differenceArray

def findDifferenceArray(nums):
    n = len(nums)
    leftSum = [0] * n
    rightSum = [0] * n
    differenceArray = [0] * n
    
    # Calculate leftSum array
    leftSum[0] = nums[0]
    for i in range(1, n):
        leftSum[i] = leftSum[i-1] + nums[i]
    print('leftSum', leftSum)
    
    # Calculate rightSum array
    rightSum[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        rightSum[i] = rightSum[i+1] + nums[i]
    print('rightSum', rightSum)
    
    # Calculate differenceArray
    for i in range(n):
        differenceArray[i] = abs(leftSum[i] - rightSum[i])
    
    return differenceArray


def main():
    # arr = [2, 5, 1, 6]
    # arr = [3, 3, 3]
    arr = [1, 2, 3, 4, 5]
    result = findDifferenceArray(arr)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)