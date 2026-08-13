# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        '''
        Brute Force:
            Each node compute the left and right subtree height
            If the left and right are diff Return False
            Else recurse down the tree

            -> works but inefficient for very large and skewed trees

        Optimized:
            As we are computing height we figure out if subtree is balanced, 
            Send the info up immediatly

        '''

        def height_checker(root):
            if not root:
                #empty tree has height 0 is balanced
                return 0
            
            #recurse thorugh entire left subtree and check if the height
            left_height = height_checker(root.left)
            if left_height == -1:
                return -1 

            right_height = height_checker(root.right)
            if right_height == -1:
                return -1 

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return height_checker(root) != -1
            

