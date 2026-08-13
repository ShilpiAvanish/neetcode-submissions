class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])

        for row in matrix:
            
            if row[-1] >= target:
                
                l, r = 0, len(row) - 1
                while l <= r:
                    mid =  int((l + r) / 2)
                    if target > row[mid]:
                        l = mid + 1
                    elif target < row[mid]:
                        r = mid - 1
                    elif target == row[mid]:
                        return True

        return False