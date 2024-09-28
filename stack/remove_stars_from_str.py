def removeStars(strings):
    stack = []
    for char in strings:
        if stack and char == '*':
            stack.pop()
        elif char != '*':
            stack.append(char)
    return ''.join(stack)


def main():
    strings = "abc*de*f"
    # strings = "*a*b*c*d*"
    # strings = "a*b*c*d"
    # strings = "abcd"
    result = removeStars(strings)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)