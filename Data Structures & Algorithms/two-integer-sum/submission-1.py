class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for index in range(len(nums)):
            complement = target - nums[index]
            if nums[index] in hashMap:
                print(index)
                return [hashMap[nums[index]], index]
            hashMap[complement] = index

            #[4, 0]
            #[5, 1]