class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        def islandCheck(r, c):

            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"

            islandCheck(r + 1, c)
            islandCheck(r, c + 1)
            islandCheck(r - 1, c)
            islandCheck(r, c - 1)

        result = 0
        for i in range(n):
            for j in range(m):

                if grid[i][j] == "1":
                    islandCheck(i, j)
                    result += 1
        
        return result
            