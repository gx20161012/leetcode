class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int 
        n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).
        """
        len = 1
        cnt = 9
        count = 0
        while len * cnt < n:
            count += len * cnt
            len += 1
            cnt *= 10
        print(len, cnt, count)
        m = n - count
        print(m)
        if m % len == 0:
            num = 10 ** (len-1) - 1 + m // len
            return int(str(num)[len-1])
        else:
            num = 10 ** (len-1) + m //len
            r = m % len
            return int(str(num)[r-1])

s = Solution()
print(s.findNthDigit(1000))


