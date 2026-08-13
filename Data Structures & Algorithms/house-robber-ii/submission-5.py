class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        Can't Rob to adjacent houses, but now the end index and
        start index loop each other.

        Type of DP
            Max Val
        Define the DP[i]
            Max you can steal from this postion
        Decision
            Take i and skip i + 1
            skip i and take i + 1

            Run twice and find max
            Take 0 and skip [-1]
            skip [-1] and take 0
        Base Case
            dp[0] = nums[0]
        '''

        
        def rob_line(houses):
            n = len(houses)

            if n == 0:
                return 0
            if n == 1:
                return houses[0]

            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2] + houses[i], dp[i-1])

            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]

        return max(rob_line(nums[1:]),   # exclude first house
                rob_line(nums[:-1]))  # exclude last house
