def reverseString(str_char):
    par_stack = list(str_char)
    reversed_word = ''
    for _ in range(len(par_stack)):
        top = par_stack.pop()
        reversed_word += top
    return reversed_word


def main():
    string_char = "Hello, World!"
    string_char = "OpenAI"
    string_char = "Stacks are fun!"
    result = reverseString(string_char)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)