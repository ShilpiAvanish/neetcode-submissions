class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()


        def dfs(i, curr, curr_value):

            if curr_value == target:
                res.append(curr.copy())
                return

            for j in range(i, len(nums)):
                if curr_value > target:
                    return
                curr.append(nums[j])
                dfs(j, curr, curr_value + nums[j])
                curr.pop()


        
        dfs(0, [], 0)

        return res
