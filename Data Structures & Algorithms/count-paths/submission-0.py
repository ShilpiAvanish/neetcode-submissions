class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        """
            To reach bottom right you much make (m-1) moves downward
            (n-1) moves to the right = (m+n-2) moves
        """
        
        total_moves = m + n - 2

        return math.comb(total_moves, n-1)