class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:

        import bisect
        bisect.insort(self.arr, num)
        return None
        

    def findMedian(self) -> float:
        
        length = len(self.arr)
        print(self.arr)
        if length % 2 == 0:

            index, index1 = length // 2 - 1, length // 2
            avg = (self.arr[index] + self.arr[index1]) / 2
            return avg
        else:

            index = length // 2
            return self.arr[index]
