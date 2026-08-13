class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        '''
        Intuition:
            Back track through each option using dfs
        '''

        result = []
        curr = []

        # current list and index
        # r = []
        # c = []
        # i = 2
        def backtracking(index):

            result.append(curr[:])
            #r = [[], [1], [1, 2], [1,2,3], ]
            
            # i ->
            for i in range(index, len(nums)):
                curr.append(nums[i])
                #c = [1, 2, 3]
                backtracking(i + 1)
                curr.pop()

        backtracking(0)
        return result