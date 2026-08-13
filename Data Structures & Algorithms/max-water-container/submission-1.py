class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_hold = 0

        while l < r:
            if heights[l] < heights[r]:
                min_index = l
            else:
                min_index = r

            distance = r - l
            max_hold = max(max_hold, (distance * heights[min_index]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_hold





