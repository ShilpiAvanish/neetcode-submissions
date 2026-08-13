class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        '''
        Using and DSU to solve this optimally
        Start with each node as a component
        Reduce by one everytime you see a merge two components
        '''

        # each node starts as its own parent
        parent = [i for i in range(n)]


        # to help keep track of which tree attatches to which tree
        # keep track of structure
        rank = [1] * n

        # find function identifies the root of that component
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return 0
            
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootX] = rootY
                rank[rootX] += 1

            return 1
        
        components = n
        for start, end in edges:

            components -= union(start, end)

        return components


        