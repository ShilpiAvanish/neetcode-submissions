class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #global answer
        answer = []
        nums.sort()
        length = len(nums)

        def dfs(i, curr, total):

            if total == target:
                answer.append(curr.copy())
                return

            if i >= length or total > target:
                return

            # two decisions
            # first decision
            # add the ith element to current
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # second decision
            # move to next element
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return answer
