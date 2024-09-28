def makeGood(strings):
    stack = []
    for char in strings:
        if stack and stack[-1].swapcase() == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


def main():
    strings = "AaBbCcDdEeff"
    # strings = "abBA"
    # strings = "s"
    # strings = "ssTT"
    # strings = "AbCdEfghIj"
    result = makeGood(strings)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)