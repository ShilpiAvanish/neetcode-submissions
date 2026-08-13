class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROW, COL = len(grid), len(grid[0])

        # some dfs to convert the 1s to 0s after the are visisted
        def dfs(i, j):

            if (i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == "0"):
                return

            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # double for loop to go through the grid
        count = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count