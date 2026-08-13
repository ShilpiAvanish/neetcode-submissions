class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        uniqueValues = set()

        for num in nums:
            
            if num in uniqueValues:
                return True
            else:
                uniqueValues.add(num)

        return False

