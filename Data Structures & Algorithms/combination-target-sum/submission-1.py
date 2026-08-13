class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, cur, total):
            # base case we foudn the target so we add to resuts
            if total == target:
                res.append(cur.copy())
                return
            #base case we over the index or over targer so retunr
            if i >= len(nums) or total > target:
                return
            
            # the value is valid so we add to curr
            cur.append(nums[i])
            # run dfs again
            dfs(i, cur, total + nums[i])
            # clean up
            cur.pop()
            
            # second side of the tree
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


