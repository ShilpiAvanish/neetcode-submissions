class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        non_duplicate = set(nums)

        return len(non_duplicate) != len(nums)