class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            Min/Max Value
                Min # of coins to reach amount
            dp[i]
                Min # of coins to find sum i
            Base Case
                dp[0] = 0 -> make 0 amount you need 0 coins
            Iteratively
                dp[i] = min(dp[i], dp[i-c] + 1)
        '''

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for curr in range(1, amount + 1):

            for coin in coins:
                if curr - coin >= 0:
                    # check the dp at curr - each coin, and 
                    # + 1 is to add the curr coin, 

                    # for each for loop for the coins
                    # you are tyrign a new dp[curr]
                    dp[curr] = min(dp[curr], dp[curr-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1