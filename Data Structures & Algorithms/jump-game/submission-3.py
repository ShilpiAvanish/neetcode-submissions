from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
       
        n = len(nums)
        valid_index = [False] * n

        valid_index[-1] = True

        for i in range(n - 2, -1, -1):
            furthest = min(n-1, i + nums[i])
            for j in range(i + 1, furthest+1):
                if valid_index[j]:
                    valid_index[i] = True
                    break

        return valid_index[0]


        