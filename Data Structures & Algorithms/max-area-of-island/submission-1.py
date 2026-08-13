class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r, c = len(grid), len(grid[0])
        
        def dfs(i, j):


            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            
            return (1 +
            dfs(i, j + 1) +
            dfs(i, j - 1) +
            dfs(i + 1, j) +
            dfs(i - 1, j)
            )




        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(dfs(i, j), max_area)
        
        return max_area
