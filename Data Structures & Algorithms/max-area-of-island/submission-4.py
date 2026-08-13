class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        
        def dfs(r, c):

            if r < 0 or c < 0. or r >= ROW or c >= COL or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            count = 1

            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count





        max_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_count = max(dfs(i,j), max_count)

        return max_count