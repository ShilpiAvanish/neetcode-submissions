from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2  # midpoint index
            
            # Case 1: Found target
            if nums[mid] == target:
                return mid
            
            # Case 2: Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # search left half
                else:
                    l = mid + 1  # search right half
            
            # Case 3: Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # search right half
                else:
                    r = mid - 1  # search left half
        
        return -1  # target not found