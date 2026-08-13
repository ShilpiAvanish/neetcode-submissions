class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_max = 0

        # goes through all the heights
        def dfs(curr):
            if not curr:
                return 0
            
            # gets height from left and right sub tree
            left = dfs(curr.left)
            right = dfs(curr.right)

            # finds the max between current max diamter and potential new one
            self.global_max = max(left + right, self.global_max)

            # add edge to new height for left or right side
            return 1 + max(left, right)

        # running method
        dfs(root)

        # return global value of max height
        return self.global_max
