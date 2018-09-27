'''
Given a column title as appear in an Excel sheet, return its corresponding column number
'''
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        sum = 0
        for i in range(length):
            sum += (ord(s[length-1-i]) - 64) * (26 ** i)
        return sum
s = Solution()
print(s.titleToNumber('ZY'))       