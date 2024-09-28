def sortStack(stack):
    tempStack = []
    while stack:
        top = stack.pop()
        while tempStack and tempStack[-1] > top:
            top_tempStacks = tempStack.pop()
            stack.append(top_tempStacks)
        tempStack.append(top)

    return tempStack


def main():
    stack = [34, 3, 31, 98, 92, 23]
    # stack = [4, 3, 2, 10, 12, 1, 5, 6]
    # stack = [20, 10, -5, -1]
    result = sortStack(stack)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n^2)
# space_complexity = O(n)