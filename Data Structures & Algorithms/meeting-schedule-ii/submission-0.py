"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start_arr = sorted(interval.start for interval in intervals)
        end_arr = sorted(interval.end for interval in intervals)

        count = 0
        max_count = 0
        s = e = 0

        while s < len(intervals):

            if start_arr[s] < end_arr[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            
            max_count = max(max_count, count)

        return max_count