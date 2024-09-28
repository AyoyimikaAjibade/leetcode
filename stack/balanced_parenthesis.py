def isValid(str_char):
    par_stack = []

    for char in str_char:
        if char in ['{', '[', '(']:
            par_stack.append(char)
        else:
            if not par_stack:
                return False
            top = par_stack.pop()
            if char == ')' and top != '(':
                return False
            if char == '}' and top != '{':
                return False
            if char == ']' and top != '[':
                return False
    return not par_stack


def main():
    string_char = "{[()]}"
    string_char = "{[}]"
    string_char = "(]"
    result = isValid(string_char)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)