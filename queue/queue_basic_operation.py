class Node:
    # Node class for storing data and the reference to the next node
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # Queue class using linked list
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        # Add an element to the rear of the queue
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        # Remove an element from the front of the queue
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.data

    def peek(self):
        # Get the front element of the queue
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0

    def get_size(self):
        # Get the number of elements in the queue
        return self.size
    
class CircularQueue:
    # Constructor to initialize the queue
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # Function to insert an element in the queue
    def enqueue(self, element):
        if ((self.front == 0 and self.rear == self.size - 1) or
                (self.rear == (self.front - 1) % (self.size - 1))):
            print("Queue is Full")
        elif self.front == -1:  # Insert First Element
            self.front = self.rear = 0
            self.queue[self.rear] = element
        elif self.rear == self.size - 1 and self.front != 0:
            self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1)
            self.queue[self.rear] = element

    # Function to delete an element from the queue
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return None

        data = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return data

    # Function to display the elements of the queue
    def displayQueue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        print("Elements in the Circular Queue are: ")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()