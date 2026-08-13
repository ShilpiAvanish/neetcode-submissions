class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        


        # [a, b] -> b is a prereq to a

        # create a hashmap to see all the pre reqs a certain course has
        prereq_map = defaultdict(list)
        visit_set = set()

        for req, prereq in prerequisites:

            prereq_map[req].append(prereq)

        def dfs(value):
            # base case found leaf
            if value in visit_set:
                return False
            if prereq_map[value] == []:
                return True

            visit_set.add(value)

            for vals in prereq_map[value]:
                if not dfs(vals): return False
            visit_set.remove(value)
            prereq_map[value] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True




        # have to do some sort of dfs to make sure I do not got back 
        # to same spot (check if no loop)

        # you have number of courses so if you go over numbher of courses you are now in loop