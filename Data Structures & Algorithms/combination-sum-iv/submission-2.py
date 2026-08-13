class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''   
        Brute Force:
        Try evvery possible sequence by recursively subtracting nums from target
        Base Case: target == 0, valid combination

        Time complex: number of letters ^ target / Nums left

        Key Insight:
        You are repeatedly needing results for a smaller target
            -> (target - num)
        
        Instead of recomputing, store results in DP

        Steps:
        1. dp[t] -> # of ways to reach sum t
        2. Base Case -> dp[0] = 1 (empty sequence)
        3. Each index sum of dp[t - num]
        4. Answer = dp[target]
        '''  

        # dp[i] -> num of ways to reach sum i
        dp = [0] * (target + 1)
        # base case: 1 way to make a sum of 0
        dp[0] = 1
        # iterate through each index of the dp table startign from 1
        for i in range(1, target + 1):
            # iterate over each num in nums:
            # iterate over each index postion and add to new dp index
            for num in nums:
                # check if the from that index if the value of num is greater than 0
                # make sure it is a postive index vluae
                if i - num >= 0:
                    # add that potentail ways to reach that index + new way to the new index position
                    dp[i] += dp[i - num]
            #return the final target index
        return dp[target]


        '''
        tim -> O(target * target)
        Space -> 0(target) -> o(1)
        '''