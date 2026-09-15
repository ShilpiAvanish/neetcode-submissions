class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        '''
            Need to be able to partition list into 2 subsets
            where both subsets have the same sum


            DP quetion
            type -> True/False, whether it is possible
            define dp[] -> can we create a subset with sum == total sum // 2
            dp state -> true if we can create subset with sum using numbers we proccessed
            target -> dp[target] -> return true or false


            Base Case -> if total sum is odd, we cannot split evenly
            dp[0] = true -> always create a sum of noting
        '''


        total = sum(nums)

        if total % 2 == 1:
            return False


        target = total // 2


        dp = [False] * (target + 1)


        dp[0] = True

        # process each number exactly once
        for num in nums:

            # go through backwards so we dont use number twice
            for s in range(target, num - 1, -1):

                # we can make s if we already make s or
                # we could make s - num and now add num
                dp[s] = dp[s] or dp[s-num]


        return dp[target]



