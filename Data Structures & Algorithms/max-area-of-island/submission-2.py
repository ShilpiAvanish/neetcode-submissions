class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        '''

        Maintain a max to handle the max area of a island

        Run DFS to indentify the max area size

        then compare with existing max

        for loop through the entire grid

        '''

        n = len(grid)
        m = len(grid[0])
        max_area = 0

        def dfs(i , j):
            
            if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] != 1:
                return 0

            
            grid[i][j] = 0

            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)


        for i in range(n):
            for j in range(m):
                
                if grid[i][j] == 1:
                    max_area = max(dfs(i , j), max_area)

        return max_area
