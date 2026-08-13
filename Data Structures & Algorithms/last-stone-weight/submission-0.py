class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # put all the stones within the max heap (negated min heap)

        stones = [-s for s in stones]

        # turn into a heap that takes o(n)
        heapq.heapify(stones)

        # keep smashing until 0 or 1 stone left
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # if not equal push difference3
            if first != second:
                heapq.heappush(stones, -(first-second))

        # if one stone remains return it or return 0
        return -stones[0] if stones else 0

