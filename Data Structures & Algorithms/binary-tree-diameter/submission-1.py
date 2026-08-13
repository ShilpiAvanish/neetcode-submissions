class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_max = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.global_max = max(left + right, self.global_max)
            return 1 + max(left, right)

        dfs(root)
        return self.global_max
