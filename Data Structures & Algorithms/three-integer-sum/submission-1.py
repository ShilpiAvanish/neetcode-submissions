class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_result = []

        # Sort the array to use the two-pointer approach
        nums.sort()

        for i in range(len(nums)):
            # If the current number is greater than 0, break (no valid triplets)
            if nums[i] > 0:
                break
            
            # Skip duplicate numbers to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # Calculate the current sum
                total_summation = nums[i] + nums[left] + nums[right]

                if total_summation == 0:
                    # If sum is 0, add triplet to the result
                    final_result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total_summation < 0:
                    # If sum is less than 0, move the left pointer right
                    left += 1
                
                else:
                    # If sum is greater than 0, move the right pointer left
                    right -= 1

        return final_result