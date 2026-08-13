class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        number_set = set(nums)

        max_consecutive = 0
        for num in number_set:
            
            

            if num - 1 in number_set:
                continue
            
            consecutive = 1
            while num + 1 in number_set:
                consecutive += 1
                num += 1
            
            max_consecutive = max(consecutive, max_consecutive)

        return max_consecutive


        