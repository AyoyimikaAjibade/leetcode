def removeDuplicates(strings):
    stack = []
    for char in strings:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


def main():
    strings = "abbaca"
    # strings = "azxxzy"
    # strings = "abba"
    result = removeDuplicates(strings)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)