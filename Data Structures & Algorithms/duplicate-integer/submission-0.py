class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = {}
        for num in nums:
            if num in keys:
                return True
            else:
                keys[num] = 1
        return False