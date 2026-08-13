# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # checks if valid subtree
        def valid_subtree(root, subroot):
            
            # check if root node or nothing there
            if not root and not subroot:
                return True
            
            # if both nodes valid check if they are the same
            if root and subroot and root.val == subroot.val:
                #if they are the same go left and go right and try again
                return (valid_subtree(root.left, subroot.left) and valid_subtree(root.right, subroot.right))
        
        # if sub root empy let it be
        if not subRoot:
            return True
        # if not tree return False
        if not root:
            return False
        
        # if the subtree is valid reutrn false
        if valid_subtree(root, subRoot):
            return True
        # if not go left and right and see if any return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        




