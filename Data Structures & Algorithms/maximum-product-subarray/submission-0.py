class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        '''
        
        Type of DP
            Max Value
        Dp[i] gonna have two
            max_dp -> keep track of max product ending at index i
            min_dp -> keep track of min product ending at index i
        Base Case
            dp[0] = 0
            dp[0] = 0
            global_max = nums[0]
        Iteratively
            each index i
                start a new subarray
                extend prev max product
                extend prev min product
        '''

        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            if n < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)

            global_max = max(global_max, curr_max)
        
        return global_max