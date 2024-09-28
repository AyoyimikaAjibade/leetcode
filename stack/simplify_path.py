def simplifyPath(path):
    stack = []
    for comp in path.split('/'):
        if comp == '..':
            if stack:
                stack.pop()
        elif comp and comp != '.':
            stack.append(comp)
    return '/' + '/'.join(stack)


def main():
    path = "/a//b////c/d//././/.."
    path = "/../"
    path = "/home//foo/"
    result = simplifyPath(path)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)