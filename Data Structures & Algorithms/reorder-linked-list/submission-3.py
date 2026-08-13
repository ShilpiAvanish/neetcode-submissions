# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # have a pointer skip every pointer, go twice every once
        # reverse on the second pointer
        # feed into first pointer

        slow = head
        fast = head.next

        # not sure if this is right
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # figure out how to reverse the nodes
        second = slow.next
        prev = slow.next = None


        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # add reversed to the front, curr is holding head

        front = head
        second = prev

        while second:
            temp1, temp2 = front.next, second.next
            front.next = second
            second.next = temp1
            front, second = temp1, temp2
