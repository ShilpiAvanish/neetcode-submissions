class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        '''
        Brute force -> mulitple x by itself n times


        Binary Exponentiation

        2^10 -> (2^5)^2
        2^5 -> (2^2)^2 x 2
        2^2 -> 2^1 ^2

        When n is even

        x^n -> (x^2)^(x/2)

        When n is odd

        x^n = x * x^(n-1)
        '''

        if n < 0:
            x = 1 / x
            n = -n

        result  = 1.0

        while n > 0:

            # check if odd then multiple by value of x
            if n % 2 == 1:
                result *= x


            x *= x

            n //= 2


        return result