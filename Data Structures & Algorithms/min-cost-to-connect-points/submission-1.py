class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        we are going to try to connect all the points using x, y as costs

        Use a min-heap to store all the distances from each node

        push all the distances from one node to all nodes into heap

        pop smallest point and connec those points

        repeat this proccess
        '''

        n = len(points)
        visited = set()
        minHeap = [(0, 0)]
        total_cost = 0

        while len(visited) < n:

            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            
            visited.add(i)
            total_cost += cost

            for j in range(n):
                
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(minHeap, (dist, j))

        return total_cost




