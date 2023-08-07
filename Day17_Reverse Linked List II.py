# Reverse Linked List II                            Difficulty = Medium

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Comparing with Problem 206: just need to find the start position 
        # then reverse (same as 206)
    
        dummy = ListNode(0)
        dummy.next = head
    
        pre = dummy
        cur = dummy.next
    
       # find the position
        for i in range(1,left):
            cur = cur.next
            pre = pre.next
    
    
       # reverse
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next  = pre.next
            pre.next = temp
    
        return dummy.next
    
    