class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])

        for row in matrix:
            
            if row[-1] >= target:
                
                for c in row:
                    if c == target:
                        return True

        return False
