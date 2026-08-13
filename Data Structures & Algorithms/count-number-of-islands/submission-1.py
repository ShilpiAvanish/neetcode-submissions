class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # dfs
        r = len(grid)
        c = len(grid[0])
        checked = set()
        def dfs(i, j):

            # check if out of bounds
            # check if already went on 
            # check if in water
            if i >= r or i < 0 or j >= c or j < 0:
                return
            if grid[i][j] == "0" or (i, j) in checked:
                return

            checked.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # iternate through the entire 2d array
        island_count = 0 
        checked = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in checked:
                    dfs(i, j)
                    island_count += 1

        return island_count
                