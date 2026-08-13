class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        '''

            iterate through each index, when a new index is 
            hit then try sum else

        '''
        result = []
        curr = []
        used = [False] * len(nums)
        def dfs():
            
            if len(curr) == len(nums):
                result.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                curr.append(nums[i])

                dfs()

                curr.pop()
                used[i] = False
            
        dfs()
        return result
