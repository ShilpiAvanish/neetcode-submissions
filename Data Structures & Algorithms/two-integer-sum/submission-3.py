class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        complement_dictionary = {}

        for i, num in enumerate(nums):

            if target - num in complement_dictionary:
                return [complement_dictionary[target-num], i]
            else:
                complement_dictionary[num] = i
        
        