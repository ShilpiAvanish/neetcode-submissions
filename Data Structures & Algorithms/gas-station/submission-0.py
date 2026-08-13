class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        '''

            brute force basically trying from each location
            and see if you can come back to same locaiton

            Start from the highest gas available

            keep track of total, curr and start

            iterate thorugh each index position to be a potential start

            find the diff
            update total 
            update curr

            if curr is less than 0 everyhting up to that will fail
            use new start and set curr to 0

            check if total gas is more that cost or willl not work

        '''

        total = 0
        curr = 0
        start = 0

        for i in range(len(gas)):

            diff = gas[i] - cost[i]
            total += diff
            curr += diff

            if curr < 0:
                start = i + 1
                curr = 0

        return start if total >= 0 else -1