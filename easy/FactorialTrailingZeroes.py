'''
Given an integer n, return the number of trailing zeroes in n!.
'''
import math
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += math.floor(float(n) / 5) 
            n /= 5
        return int(math.floor(count))

s = Solution()
count = s.trailingZeroes(4)
print(count)
