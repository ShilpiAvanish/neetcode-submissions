class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #measures the amount of times the value shows up
        frequencyTable = {};

        #creates the bucket
        bucket = [[] for _ in range(len(nums) + 1)];


        #fills out the frequency table
        for num in nums:
            frequencyTable[num] = 1 + frequencyTable.get(num, 0);
        
        for num, freq in frequencyTable.items():
            bucket[freq].append(num);
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for value in bucket[i]:
                result.append(value);
                if k == len(result): 
                    return result
