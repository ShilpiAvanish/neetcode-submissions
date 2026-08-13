class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''

        Input:
            position -> array with cars of i starting at position[i] 
            speed -> array with cars of i speed speed[i]
            target -> int containing the final destination of the car

        Constraints:
            If a car catches up to another car/fleet it joins that fleet
        
        Output:
            Return the number of cars or  carfleets end up reaching target

        Solution:
            Only thing that matter is the time they reach the target
                -> (target - position) / speed -> time
            
            Sort the car's time in descending order, descending -> closest to target first
            Compute each car's time to reach the target
            Iteration to traverse the from the car closests to target backwards:
                if a car takes more time than fleet ahead -> create new fleet
                otherwise -> merge with the fleet ahead
        '''
        # create tuples for the cars to hold the position and the speed
        cars = sorted(zip(position, speed), reverse = True)
        # fleets -> store the num of fleets
        fleets = 0
        # pre_time -> track slowest fleet time seen so far
        prev_time = 0
        for pos, speed in cars:
            
            # time untill target reached
            time = (target - pos) / speed

            # if the car can catch up to the fleet ahead
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets

