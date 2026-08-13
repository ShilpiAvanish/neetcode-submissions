class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        oppo_dict = {}


        for i, num in enumerate(nums):

            oppo = target - num

            if oppo in oppo_dict:
                return [oppo_dict[oppo], i]

            oppo_dict[num] = i