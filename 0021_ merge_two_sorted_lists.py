#21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Steps to solve:
# 1. Initialize and create a dummy node prehead which will help to simplify edge cases like merging empty lists.
# 2. Iterating through both list1 and list2 we will
#  i. Use a pointer 'previous' initialized to prehead.
#  ii. Compare the current nodes of both lists (list1 and list2).
#  iii. Attach the smaller node to the previous pointer and move the pointer in the respective list forward.
#  iv. Move the previous pointer forward to continue building the merged list.
# 3. When attaching the remaining nodes when on of the list is empty, attach the remaining nodes of the other list to the merged list.
# 4. Return the merged list

# time complexity = o(n + m)
# space complexity = o(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    prehead = ListNode(-1)
    previous = prehead

    while list1 and list2:
        if list1.val < list2.val:
            previous.next = list1
            list1 = list1.next
        else:
            previous.next = list2
            list2 = list2.next
        previous = previous.next

    previous.next = list1 or list2

    return prehead.next

# Creating list1 out of array [1,2,4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Creating list2 out of array [1,3,4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
#output 1 -> 1 -> 2 -> 3 -> 4 -> 4 ->

# array1 = []
# array2 = [] #output []
# array1 = []
# array2 = [0] #output [0]
merged_list = mergeTwoLists(list1, list2)
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next


