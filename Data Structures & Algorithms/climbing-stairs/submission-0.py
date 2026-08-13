class Solution:
    def climbStairs(self, n: int) -> int:
        
        # steps = [1,2]

        # num_steps = [0] * n

        # nums_steps[0] = 1
        # nums_steps[1] = 2

        # for i , num in enumerate(2, n):

        #     nums_steps[i] += 1 + nums_steps[i - steps[0]]
        #     nums_steps[i] += 1 + nums_steps[i - steps[1]]

        # return nums_steps[n]

        if n == 1:
            return 1
        if n == 2:
            return 2

        num_steps = [0] * (n)
        num_steps[0] = 1
        num_steps[1] = 2

        for i in range(2, n):
           
            num_steps[i] = num_steps[i - 1] + num_steps[i - 2]

        return num_steps[n - 1]