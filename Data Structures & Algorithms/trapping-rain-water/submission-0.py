class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]

        while left < right:
            # if maxL is great we increase left by one
            if maxL <= maxR:
                left += 1
                # find the new max if applies
                maxL = max(maxL, height[left])
                # caucluate the new total water
                total_water += max(0, maxL - height[left])
            else:
                # move right pointer
                right -= 1
                # see if identified to max right
                maxR = max(maxR, height[right])
                # caculate if new water total is identified
                total_water += max(0, maxR - height[right])

        return total_water
