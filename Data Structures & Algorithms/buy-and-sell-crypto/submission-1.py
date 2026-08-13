class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        finalResult = 0

        leftPointer = prices[0]

        for price in prices:
            rightPointer = price
            if rightPointer < leftPointer:
                leftPointer = price
            
            finalResult = max(finalResult, rightPointer - leftPointer)
        
        return finalResult