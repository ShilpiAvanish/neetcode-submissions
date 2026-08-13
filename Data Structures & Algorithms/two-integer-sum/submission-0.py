class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for index in range(len(nums)):

            num = nums[index]
            inverseTarget = target - num
            if inverseTarget in hashMap:
                return [hashMap[inverseTarget], index]
            hashMap[num] = index

        return []

        