from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        '''

            Run BFS from each Treasure Chest, and find the min for,
            each cell,

            Run For loop through, when you find a treasure ches,
            run a bfs, & update each cell to lowest point

            Then you have the udpated output

        '''





        n = len(grid)
        m = len(grid[0])

        q = deque()
        
        # add all the treasure chests to the queue cause that
        # is where we will start
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            i, j = q.popleft()
            for di, dj in dirs:

                x, y = i + di, j + dj

                if 0 <= x < n and 0 <= y < m and grid[x][y] != -1:

                    if grid[x][y] > grid[i][j] + 1:
                        grid[x][y] = grid[i][j] + 1
                        q.append((x, y))