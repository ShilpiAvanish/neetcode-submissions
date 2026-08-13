from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # farthest index we can reach so far
        maxReach = 0  
        
        # iterate through each index
        for i, jump in enumerate(nums):
            # if current index is out of reach, we can't continue
            if i > maxReach:
                return False
            
            # update the farthest reach
            maxReach = max(maxReach, i + jump)
            
            # if we can reach or pass the last index
            if maxReach >= len(nums) - 1:
                return True
        
        # after loop, check if we reached the end
        return maxReach >= len(nums) - 1