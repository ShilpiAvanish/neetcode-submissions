class MedianFinder:

    def __init__(self):

        # use a a priority queue to help manage the ordering of a list
        self.sorted_list = []
        self.length = 0

    def addNum(self, num: int) -> None:
        
        self.sorted_list.append(num)
        self.sorted_list.sort()
        self.length += 1


    def findMedian(self) -> float:
        
        index = self.length // 2

        if self.length % 2 == 0:
            return (self.sorted_list[index] + self.sorted_list[index - 1]) / 2
        else:
            return self.sorted_list[index]
        

        