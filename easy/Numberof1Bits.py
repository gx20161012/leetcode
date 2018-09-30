'''
Write a function that takes an unsigned integer and 
returns the number of '1' bits it has (also known as the Hamming weight).
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str1 = str(bin(n))
        return list(str1).count('1')


s = Solution()
print(s.hammingWeight(127))