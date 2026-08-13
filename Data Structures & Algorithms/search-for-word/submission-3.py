class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row, col = len(board), len(board[0])
        visited_set = set()

        def dfs(i, j, index):
        
            if index == len(word):
                return True
            
            if i >= row or i < 0 or j >= col or j < 0 or board[i][j] == "#" or      word[index] != board[i][j]:
                return False

            board[i][j] = "#"
            
            res = (dfs(i+1,j, index+1) or
            dfs(i-1,j, index+1) or
            dfs(i,j+1, index+1) or
            dfs(i,j-1, index+1))

            board[i][j] = word[index]

            return res



        # start at each position and run dfs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False