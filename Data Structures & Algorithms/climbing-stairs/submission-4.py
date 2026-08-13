class Solution:
    def climbStairs(self, n: int) -> int:
    
        ''' 
        Max/Min
        Counting Ways ***
        True/False Feasilbity
        Subsequence Build-Up

        Intuition for Counting Ways ->
            Define the dp[i] meaning
                dp[i] = max # of ways I can reach dp[i]
            Build the Recrusion
                What decision leads to dp[i]
                both dp[i-1] + 1 and dp[i-2] + 2
            Base Case
                dp[0] = 1
                dp[1] = 1
            Fill up & Return
                Computer dp from 2 to n
        '''

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            print(dp[i-1] + 1)
            print(dp[i-2] + 1)
            dp[i] = (dp[i-1]) + (dp[i-2])

        print(dp)
        return dp[n]