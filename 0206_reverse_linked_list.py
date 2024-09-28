#206. Reversed Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Steps to solve:
# 1. Initialize three variables  
#  i. previous set to None, this will become the new end of the list
#  ii. current is set to head, which will used to traverse the list
# 2. Iterate through the list.
# 3. next_temp stores the next node (current.next). This step is crucial because we are about to change current.next.
# 4. Reverse the pointer of the current node (current.next = previous).
# 5. Move the previous pointer to the current node (previous = current).
# 6. Move the current pointer to the next node (current = next_temp).
# 5. Return the new head which will reverse the list.

# time complexity = o(n)
# space complexity = o(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


head = [1,2,3,4,5] #output [5,4,3,2,1]
# head = [1,2] #output [2,1]
# head = [] #output []
print(reverseList(head)) 