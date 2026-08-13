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
        #works backwards from the start
        for i in range(len(bucket) - 1, 0, -1):
            #for each value in the list within the list
            for value in bucket[i]:
                #add to answer
                result.append(value);
                #check if the final answer is there and return
                if k == len(result): 
                    return result
