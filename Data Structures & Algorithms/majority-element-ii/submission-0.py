class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''

        Input:
            arr -> nums
        
        Goal:
            Find and return all the values that have a freq of n/3 or more

        nums = [5,2,3,2,2,2,2,5,5,5]
        min_freq = 10/3 = 3
        return order does not matter
        return -> [5, 2]

        if no values hit that min freq
        -> return empty list

        Brute Force:
            Count the freq of each number -> dictionary or counter
            collection the number of numbers with freq > n/3
            Time -> O(n)
            Space -> O(n)

        Efficient Solution:
            Only keeping track of 2 of the majority elements -> reduce the space
            It is impossible 3 majority elemetns to fit the paramters of n/3
            Steps
                Iterate through the Array once
                    Increment the count of candidate every time we see it

                    If the count is 0 we will replace it with current number

                        Or we will decrement both counts bc more freq value
                Validate if these 2 most candidate actully suffice the freq restriction
                we do not know for sure
        '''


        # initisl values for the candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        n = len(nums)
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 is not None and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result
