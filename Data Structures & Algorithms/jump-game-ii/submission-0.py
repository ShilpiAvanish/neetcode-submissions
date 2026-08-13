class Solution:
    def jump(self, nums: List[int]) -> int:
        
        '''
            maintian how many jumps
            and the end of the range and the farthest we can reach

            Inedinty the farthest position we can jump to

            if we reach the end of our window
                we add a jump and update the window to the new farthest jump
        '''

        jumps = 0
        end = 0
        farthest_reach = 0

        for i in range(len(nums) - 1):

            farthest_reach = max(farthest_reach, nums[i] + i)

            if i == end:
                jumps += 1
                end = farthest_reach

        return jumps