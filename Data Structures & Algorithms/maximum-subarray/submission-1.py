class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # first get the first value and store the sum
        maxSub, currSum = nums[0], 0
        # loop throught
        for num in nums:
            # if cursum is less than 0
            if currSum < 0:
            # reate new sub array
                currSum = 0
            # add new value to subarray
            currSum += num
            # figure it valud new max
            maxSub = max(maxSub, currSum)
        # return max
        return maxSub

