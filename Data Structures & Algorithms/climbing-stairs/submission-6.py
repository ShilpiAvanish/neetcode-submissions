class Solution:
    def climbStairs(self, n: int) -> int:

        # number of distinct ways to climb staircase

        # [1] [2] [3] [(2) + 1 + 1 / (2) + 2 / (3) + 1] [] []
        if n <= 2:
            return n
        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
