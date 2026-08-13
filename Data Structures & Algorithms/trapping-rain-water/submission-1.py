class Solution:
    def trap(self, height: List[int]) -> int:
        
        '''
            Input:
                Given an array of diff height elevations

            Goal:
                Identify the max area water can be trapped
            
            Output:
                The amount of water that can be held
            
            Intuition:
                We never need to hold the full left and right arrays
                we can be smart on how we scan the array

                If the left_max is less than right_max, the limiting
                factor is left_max 

                So in that case the amount of water at index is
                left_max - height[index]

                Same logic for the right_max
        '''
        
        # if less than 3 bars, cannot hold water
        if len(height) < 3:
            return 0
        
        # keep track of the index we are on
        left = 0
        right = len(height) - 1

        # keep track of the max left and right side
        left_max = 0
        right_max = 0

        total_water = 0


        while left <= right:

            # with new left & right have to update the running max

            if height[left] > left_max:
                left_max = height[left]
            if height[right] > right_max:
                right_max = height[right]

            # handle two cases

            # if left_max <= right max
            if left_max <= right_max:
                trapped_here = left_max - height[left]

                total_water += trapped_here

                left += 1


            # if right_max < left_max
            else:

                trapped_here = right_max - height[right]

                total_water += trapped_here

                right -= 1

        return total_water





