class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # hold the len of items
        ROW, COL = len(board), len(board[0])
        # hold the set for paths taken
        paths = set()

        def dfs(r, c, i):
            
            #potential - 1
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or 
                r >= ROW or c >= COL or
                (r, c) in paths or 
                word[i] != board[r][c]):
                return False

            paths.add((r, c))
            result = (dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            # make sure paths is empty before goes to next letter
            paths.remove((r, c))
            return result

        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False


        