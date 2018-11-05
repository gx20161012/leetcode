class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = 1
        while n > index:
            n -= index
            index += 1
        if n == index:
            return index
        else:
            return index-1
s = Solution()
print(s.arrangeCoins(10))