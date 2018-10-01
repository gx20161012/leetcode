import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        for i in range(2, math.ceil(n ** 0.5), 1):
            if primes[i]:
                for j in range(i ** 2, n, i):
                    primes[j] = False
        return sum(primes) 
s = Solution()
print(s.countPrimes(20))