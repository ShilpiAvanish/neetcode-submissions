class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for index, n in enumerate(nums):
            complement = target - n
            if n in hashMap:
                return [hashMap[n], index]
            hashMap[complement] = index
