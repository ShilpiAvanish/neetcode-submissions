from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, previous_height):
            # Stop if out of bounds, already visited,
            # or the current cell is lower than the previous cell.
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or (r, c) in visited
                or heights[r][c] < previous_height
            ):
                return

            visited.add((r, c))
            current_height = heights[r][c]

            dfs(r + 1, c, visited, current_height)
            dfs(r - 1, c, visited, current_height)
            dfs(r, c + 1, visited, current_height)
            dfs(r, c - 1, visited, current_height)

        # Top and bottom edges
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # Left and right edges
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result