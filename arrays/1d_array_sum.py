def runningSum(nums):
    result = [0] * len(nums) 
    previous_result = 0 
    for i in range(len(result)):
        result[i] = nums[i] + previous_result  # add current number to previous result
        previous_result = result[i]
    return result

# def runningSum(nums):
#     result = [0] * len(nums)  
#     result[0] = nums[0]  # First element is the same
#     for i in range(1, len(nums)):  # Start from the second element
#         result[i] = result[i-1] + nums[i]  # Add current number to the previous sum
#     return result


def main():
    # arr = [3, 5, 7, 9, 11]
    # arr = [2, 3, 5, 1, 6]
    # arr = [1, 1, 1, 1, 1]
    arr = [-1, 2, -3, 4, -5]
    result = runningSum(arr)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(1)

    
