#Implement int sqrt(int x).
#Compute and return the square root of x, 
# where x is guaranteed to be a non-negative integer.
#Since the return type is an integer, 
#the decimal digits are truncated and only the integer part of the result is returned.
import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        x1 = 0.0
        x2 = 1.0
        while abs(x1 - x2) > 0.0000000000001:
            x1 = x2
            x2 = x1 / 2 + x / (2 * x1)

        return math.ceil(x1)
s  = Solution()
print(s.mySqrt(8))
            