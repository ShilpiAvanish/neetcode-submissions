class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        '''

        create the adjacency matrix then with that info
        Topological sort on the adjacency matrix
        run a dfs/bfs and make sure it works??

        '''
        # in-degree matrix
        
        graph = {i : [] for i in range(numCourses)}

        # indegree array
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # courses that have no pre reqs
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        taken = 0

        while q:
            node = q.popleft()
            taken += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return taken == numCourses

        '''
        Time Complexity:
            0(n + n + (N nodes x E edges))

        Space Complexity:
            o(n + n + E)
        '''


        



        