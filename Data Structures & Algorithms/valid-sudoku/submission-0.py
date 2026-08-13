class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue
                
                val = board[row][col]

                if val in rows[row]:
                    return False
                rows[row].add(val)

                if val in cols[col]:
                    return False
                cols[col].add(val)

                if val in box[row//3][col//3]:
                    return False
                box[row//3][col//3].add(val)

        return True

