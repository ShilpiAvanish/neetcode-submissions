class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Input:
            Array -> You are given heights of diff histograms

        Goal:
            Identify the largest rectangle you can make

        Output:
            The largest rectangle size

        Intuition:
            For each bar how left can we extend before hitting
            a smaller bar
                How right can we extend before hitting a smaller bar

            We dont want to keep on recomputing
                -> montonic increasing stack

            Key Pattern
                keep indices of bars in increasing height order
                when shorter bar appears, stops the taller bars from expanding
            
        Step by Step
            maintain a stack of indices with increasing heights

            When current bar is shorter than the top of stack
                pop the stack
                identfied its right boundry
            
            New top of stack is the left boundry

            Compute area
        '''

        # will store the indices of bars
        stack = []

        max_area = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                h = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, h * width)
            
            stack.append(i)

        return max_area