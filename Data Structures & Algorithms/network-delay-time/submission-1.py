class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''

            Create a hash map handling all thd n

            Do some sort of djkstra and find the max value from that?

            1 -> create the adjaceny list
            2 -> create a distance array to keep track of shortest distance
                    set all to infinity first
            3 -> 

            adj list -> for each index see how many prereq it has

        '''

        adj_list = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj_list[u].append((v, w))

        # expand to the next closest node first
        minHeap = [(0, k)]

        # track of shortest known distance from k
        distance = {i: float("inf") for i in range(1, n + 1)}
        distance[k] = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if time > distance[node]:
                continue

            for nei, w in adj_list[node]:
                newTime = time + w

                if newTime < distance[nei]:
                    distance[nei] = newTime
                    heapq.heappush(minHeap, (newTime, nei))

        res = max(distance.values())
        return res if res < float("inf") else - 1