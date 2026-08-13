class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # build a max heap
        # the smash the top 2 stones tg
            # if same than destry
            # if one is less than greater - less and psuh

        # return weight of last remain stone of if none remaien
        max_heap = []
        heapq.heapify(max_heap)

        for stone in stones:

            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:

            first_stone = abs(heapq.heappop(max_heap))
            second_stone = abs(heapq.heappop(max_heap))

            if first_stone == second_stone:
                continue
            else:
                new_stone = abs(first_stone - second_stone)
                heapq.heappush(max_heap, -new_stone)

        return abs(max_heap[0]) if len(max_heap) > 0 else 0