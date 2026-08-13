class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            some sort of topological sort again

            Some how keep track of which nodes we visited during our
            dfs and if we already visited we have a cycle

            use a hashset to check if we visted during the dfs
        '''

        graph = {i: [] for i in range(n)}
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True

    
        return dfs(0, -1) and len(visited) == n