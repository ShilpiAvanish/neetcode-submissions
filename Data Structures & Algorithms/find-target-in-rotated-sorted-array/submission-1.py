class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''

        one side is always sordet
        use binary search to see which half is sorter
        check if target lies in sorted array

        '''
        l, r = 0, len(nums) - 1
        # cmpute the mid arrra
        while l <= r:

            mid = (l + r) // 2
        # mid of the array contian target
            if nums[mid] == target:
                return mid
            # return mid

            # left half of the arr is sorted
            if nums[l] <= nums[mid]:
                # binary search
                if nums[l] <= target < nums[mid]:
                    # search the left half
                    r = mid - 1
                else:
                    # serach the riight half
                    l = mid + 1
            # if the right half of the arr is sorted
            else:
                if nums[mid] <= target <= nums[r]:
                    # search the left half
                    l = mid + 1
                else:
                    # serach the riight half
                    r = mid - 1

        return -1

        
