# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # intialize and prev node 
        prev = None

        # initialize a curr node
        curr = head

        while curr:

            #get the node after current
            next_node = curr.next

            #set the cur next to the prev
            curr.next = prev

            # move node to prev
            prev = curr
            # move cur to next_node
            curr = next_node

        return prev
        