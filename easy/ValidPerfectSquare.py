class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

s = Solution()
print(s.isPerfectSquare(121))