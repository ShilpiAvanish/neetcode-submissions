class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        '''

            Greedy approach

            if total gas < total cost -> impossible from wherever we start

            say we start from a location to another location and we fail, we know that between those two location we will always faile
        '''

        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):

            difference = gas[i] - cost[i]

            total += difference

            tank += difference

            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1

        return start