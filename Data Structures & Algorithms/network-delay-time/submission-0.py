class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ''' 

        Input:
            List of List: times -> ui: source node, vi: target node, ti: time
            it takes from source to target

            int: n -> number of nodes

            int: k -> the node the signal starts from

        Goal:
            Return the min time it takes for all nodes to get signal
            Return -1 if impossible, for every node to get signal
        
        Brute Force:
            Try all possible path from k to every node, compute the smallest
            total travel for each path
                Use Dfs to accumulate the costs and track min cost for each node
            
            Complexity -> O(N!) explore each path, 
            Space -> O(N) recursive call stack
        
        Dijkstra's Algo:

            Represent the graph as a adj list
                Allows us know identfiy the nei for each node
            
            Maintain a min-heap (time, node) pairs
                keep track of the shortes time between nodes
            
            Pop the node with the smallest time

            For each neighbor, if the new time < saved time, update it and push to heap

            When this is fully done, check the max time over all nodes -> how 
            long the last node to receive a signal

            check if node was never visited return -1
        '''

        # make the adjacency list
        graph = {i: [] for i in range(1, n+1)}
        # get the start node, end node, time
        for u, v, w in times:
            graph[u].append((v,w))

        # initialize a min-heap so we know which node to visit next (shortest time)
        heap = [(0, k)]
        dist = {}

        # dijkstras algo
        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue
            dist[node] = time

            # visite nei
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + wt, nei))

        if len(dist) == n:
            return max(dist.values())
        return -1
        


