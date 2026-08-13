# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        while root:
            # If both nodes are greater than root, search right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # If both nodes are smaller than root, search left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                # Found the split point or one node is the root itself
                return root