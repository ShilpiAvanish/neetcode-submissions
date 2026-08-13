class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       
        '''

        Dfs w Back Tracking

        Each Index 2 Options
        1 -> Take the number
        2 -> Skip the number

        DFS -> explore paths that can reach target
        Prune -> if goes over then stop
        Using an index pointer to prevent duplicates
        '''
        result = []
        nums.sort()
        def dfs(i, current, total):
            if total == target:
                result.append(current[:])
                return
            if i == len(nums) or target < total:
                return

            # two options

            # use current index
            current.append(nums[i])
            dfs(i, current, total + nums[i])
            current.pop()

            # skip to next index
            dfs(i+1, current, total)

        dfs(0, [], 0)
        return result