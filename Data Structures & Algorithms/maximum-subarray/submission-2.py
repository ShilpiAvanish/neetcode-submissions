class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        '''
        if new number makes the new max lower then we make smaller
        if new number makes the new max greater we add more
        '''
        max_sum = nums[0]
        running_sum = 0

        for num in nums:

            running_sum += num
            max_sum = max(running_sum, max_sum)

            if running_sum < 0:
                running_sum = 0

        return max_sum