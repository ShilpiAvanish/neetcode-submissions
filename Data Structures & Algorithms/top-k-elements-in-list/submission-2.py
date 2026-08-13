class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result_array = [[] for _ in range(len(nums) + 1)]

        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1

        for num, cnt in hashmap.items():
            result_array[cnt].append(num)

        res = []
        for i in range(len(result_array) - 1, 0, -1):
            for num in result_array[i]:
                res.append(num)
                if len(res) == k:
                    return res


