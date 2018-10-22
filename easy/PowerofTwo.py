class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt = 0
        print(128 & 1)
        while n > 0:
            cnt += (n & 1)
            n >>= 1
        if cnt == 1:
            return True
        else:
            return False

s = Solution()
print(s.isPowerOfTwo(128))