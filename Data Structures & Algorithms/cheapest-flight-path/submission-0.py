class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #easier use of the dictionary
        from collections import defaultdict
        
        #create the dictionary
        graph = defaultdict(list)

        #creating the graph of all flight connections
        for start, end, cost in flights:
            graph[start].append((end, cost))

        # stores the min cost
        min_cost = float('inf')

        #dfs algorithm
        def dfs(position: int, stops: int, cost: int):
            nonlocal min_cost
            #check if the over the number of stops or if over the min clos tlaready
            if stops > k + 1 or cost >= min_cost:
                return
            # foudn destionation and move to new min cost
            if position == dst:
                min_cost = cost
                return
            
            # recurse positon
            for neighbor, price in graph[position]:
                dfs(neighbor, stops + 1, cost + price)
        # call dfs
        dfs(src, 0, 0)
        #return value
        return -1 if min_cost == float('inf') else min_cost
