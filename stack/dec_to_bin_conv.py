def decimalToBinary(dec_num):
    stack = []
    binary_num = ''
    while dec_num != 0:
        stack.append(dec_num % 2)
        dec_num = dec_num // 2

    for _ in range(len(stack)):
        binary_num += str(stack.pop())
    return binary_num 


def main():
    num = 2
    # num = 7
    # num = 18
    result = decimalToBinary(num)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(log(n))
# space_complexity = O(log(n))