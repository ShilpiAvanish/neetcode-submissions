class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        '''

            Calculate when each car would reach the target
            -> target - postions / speed

            - bc the cars cannot pass
            -> process the cars closest to the target first

            - Car ahead that reaches in 5 hours
            - Car behind that reaches in 3 that is considered one fleet
            - Car behind reaches in 7 that is diff fleet
        '''

        cars = list(zip(position, speed))

        cars.sort(reverse=True)

        numFleets = 0

        latest_arrival_time = 0

        for pos, spd in cars:

            time = (target - pos) / spd

            # if takes longer than fleet ahead need to be a new fleet
            if time > latest_arrival_time:
                numFleets += 1

                # updates the new fleeet with cars farthes behind
                latest_arrival_time = time

        return numFleets

