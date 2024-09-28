# def reverseQueue(queue):
#     reversed_queue = []
#     for i in range(len(queue) -1, -1, -1):
#         reversed_queue.append(queue[i])
#     return reversed_queue

def reverseQueue(queue):
    stack = []
    while queue:
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    return queue


def main():
    queue_char = [1, 2, 3, 4, 5]
    # queue_char = [10, 20, 30, 40, 50]
    # queue_char = [5, 7, 9]
    queue_char = ["cat", "dog", "fish", "bird"]
    result = reverseQueue(queue_char)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)