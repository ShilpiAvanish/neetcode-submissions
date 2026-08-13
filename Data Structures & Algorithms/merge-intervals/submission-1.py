class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        '''
        
        Sort on the second index -> if the second index is greater 
        than first on next interval then merge

        '''

        intervals.sort(key=lambda x:x[0])


        # if the second index is greater than first then merge

        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):

            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])
        
        return result

