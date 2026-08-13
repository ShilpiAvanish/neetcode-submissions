class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        Type of DP Question:
            Max/Min Value
        Define DP[i]
            dp[i] = max # I can steal from 0 to i
        Recursive Decision
            2 deicions
                Take from i and skip i - 1
                Take from i - 1 and skip i
                New value = max(nums[i] + dp[i-2], dp[i-1])
        Base
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
        Compute Iteratively
            loop 2 to n
        '''

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * (n)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            print(i)
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]