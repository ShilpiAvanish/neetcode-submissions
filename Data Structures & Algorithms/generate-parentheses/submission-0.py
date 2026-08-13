class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        '''

        keep open and close vars
        adjsut vars as you use
        and try different permutations of the vars

        '''
        result = []

        def dfs(open_left, close_left, curr):

            if open_left == 0 and close_left == 0:
                result.append(curr)
                return

            # handle value for open left
            if open_left > 0:
                dfs(open_left - 1, close_left, curr+"(")
            
            if close_left > open_left:
                dfs(open_left, close_left - 1, curr+")")

            # hanle value for close left

        dfs(n, n, "")
        return result