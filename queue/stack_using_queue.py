from queue import Queue

def stack_using_queue(queue):
    operations = queue[1]
    while operations:
        queue[0].pop()
        operations -= 1
    return queue[0]

class Solution:
    def __init__(self):
        # ToDo: Write Your Code Here.
        self.main_queue = Queue()
        self.aux_queue = Queue()

    def push(self, val):
        # ToDo: Write Your Code Here.
        self.aux_queue.put(val)
        while not self.main_queue.empty():
            self.aux_queue.put(self.main_queue.get())
        self.main_queue, self.aux_queue = self.aux_queue, self.main_queue

    def pop(self):
        # ToDo: Write Your Code Here.
        return self.main_queue.get()


def main():
    queue_num = ([1, 2, 3], 2)
    # queue_num = ([9, 8], 1)
    # queue_num = ([5, 6, 7, 8], 4)
    # queue_num = (["cat", "dog", "fish"], 1)
    sol = Solution()
    sol.push(1)
    sol.push(2)
    sol.push(3)
    print(sol.pop())
    print(sol.pop())

    # result = stack_using_queue(queue_num)
    # print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(n)