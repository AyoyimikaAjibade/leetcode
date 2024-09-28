# hashmap method
def containsDuplicate(nums):
    freq_count = {}
    for i in nums:
        freq_count[i] = freq_count.get(i, 0) + 1
        if freq_count[i] > 1:
            return True
    return False

# bruteforce method
# def containsDuplicate(nums):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False

def main():
    # arr = [1, 2, 3, 4]
    arr = [1, 2, 3, 1]
    # arr = []
    # arr = [1, 1, 1, 1]
    result = containsDuplicate(arr)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity brute_force = O(n^2)
# space_complexity = O(1)

# time_complexity hash_map or sets = O(n)
# space_complexity hash_map or sets = O(n)
