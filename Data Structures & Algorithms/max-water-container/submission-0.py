class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1


        max_area = 0
        while left < right:
            distance = right - left
            min_height = min(heights[right], heights[left])

            area = distance * min_height

            max_area = max(max_area, area)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_area


            
            
