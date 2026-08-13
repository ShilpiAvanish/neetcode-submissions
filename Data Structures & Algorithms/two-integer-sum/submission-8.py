class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        Goal: 
            Use the target to indentify the value needed, store in hash
            map. Once the complement is found in the list return index
        '''
        hmap = defaultdict(int)
        
        for i, num in enumerate(nums):

            complement = target - num
            if complement in hmap:
                return [hmap[complement], i]
            
            hmap[num] = i
        
        return []