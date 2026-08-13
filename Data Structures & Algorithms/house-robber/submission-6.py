class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
        Classify DP Type:
        -> Max-Min Value

        Define dp[]:
        -> Max amount we can rob from houses 0 to i

        Base Case:
        -> No Houses
        return 0
        -> dp[0] = nums[0]
        -> Two Houses
        dp[i] = max(nums[0], nums[1])

        Recurrence Explanation
        At House i, 2 options

        Choice 1: skip house i
        -> best we can do is what we have i-1
        Choice 2: Rob house i
        -> add nums[i] and i-2

        Find the max value from these options

        '''

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])    

        return dp[-1]