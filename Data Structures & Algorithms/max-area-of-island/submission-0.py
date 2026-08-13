class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r, c = len(grid), len(grid[0])
        
        def dfs(i, j, cur_count):


            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            cur_count += 1
            
            return (1 +
            dfs(i, j + 1, cur_count) +
            dfs(i, j - 1, cur_count) +
            dfs(i + 1, j, cur_count) +
            dfs(i - 1, j, cur_count)
            )




        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(dfs(i, j, 0), max_area)
        
        return max_area
