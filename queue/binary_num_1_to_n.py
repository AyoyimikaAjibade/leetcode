from math import remainder


def generateBinaryNumbers(nums):
    queue1 = []
    queue2 = []
    num_bin = ''
    for num in range(1, nums+1):
        while num:
            remainder = num % 2
            print('num', num, remainder)
            # if not remainder == 1 and num == 0:
            num_bin += str(remainder)
            num //= 2
            print('num_bin', num_bin)
        queue1.append(num_bin)
        num = 0
        print('queue1:', queue1)
    # lst_num_bin = list(num_bin)
    # reversed_word = ''
    # for _ in range(len(lst_num_bin)):
    #     top = lst_num_bin.pop()
    #     reversed_word += top
    # queue2.append(reversed_word)
    return queue2


def main():
    numb = 2 
    numb = 3 
    # # numb = 5 
    result = generateBinaryNumbers(numb)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)