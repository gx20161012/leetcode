class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        if num > 9:
            return (num-1)%9+1
        if num < 10:
            return num
        '''
        while num // 10 > 0:
            sum = 0
            while num > 0:
                sum += num % 10
                num = num // 10
            num = sum
        return num
s = Solution()
print(s.addDigits(9999))