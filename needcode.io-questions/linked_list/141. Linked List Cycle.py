# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

#does work if there ar no duplicate values
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_values = []

        while head:
            if head.val not in visited_values:
                visited_values.append(head.val)
                head = head.next
            else:
                return True
        return False

# with duplicate values
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False
    




class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_values = set()
        cur = head

        while cur:
            if cur not in visited_values:
                visited_values.add(cur)
                cur = cur.next
            else:
                return True
        return False