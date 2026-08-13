"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        '''
            Given and list of intervals, we need to make sure that none of 
            the intervals overlap from each other:
                if does return False, True otherwise

            Sort intervals by the start time

            iterate the sorted intervals, check if the end of current does not
            overlap with next interval

            if current.end > next.start, then return False, true otherwise
        '''

        #sort the interveal on the 0th index
        intervals.sort(key = lambda x:x.start)

        # compare each itnerval with the next one

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True





