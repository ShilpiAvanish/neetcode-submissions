import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # building a max_heap which is a min_heap reversed why idk?
        freq_array = [[] for i in range(len(nums) + 1)]
        freq_count = defaultdict(int)

        for num in nums:
            freq_count[num] += 1

        for value, freq in freq_count.items():
            freq_array[freq].append(value)

        count = 0
        res = []
        for i in range(len(freq_array) - 1, 0, -1):
            for num in freq_array[i]:
                res.append(num)
                count += 1
                if count == k: return res




