class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        # Initialize prefix and postfix arrays
        prefix_array = [1] * n
        postfix_array = [1] * n
        output = [1] * n  # Result array
        
        # Compute prefix products
        for i in range(1, n):
            prefix_array[i] = prefix_array[i - 1] * nums[i - 1]
        
        # Compute postfix products
        for i in range(n - 2, -1, -1):
            postfix_array[i] = postfix_array[i + 1] * nums[i + 1]
        
        # Compute final result using prefix and postfix products
        for i in range(n):
            output[i] = prefix_array[i] * postfix_array[i]
        
        return output

        
