# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        # checks if you can do fast.next.next, if fast.next does not exist
        # then you cant do fast.next.next
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast: 
                return True

        return False