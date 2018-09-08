#Given a 32-bit signed integer, reverse digits of an integer.
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            str1 = str(x)
            list1 = list(str1)
            list1 = reversed(list1)
            str2 = ''
            for char in list1:
                str2 = str2 + char
            #print(str2)
            m = int(str2)
            if m >= -2**31 and m <= 2**31-1:
                return m
            else:
                return 0
        else:
            x = 0-x
            str1 = str(x)
            list1 = list(str1)
            list1 = reversed(list1)
            str2 = ''
            for char in list1:
                str2 = str2 + char
            #print(str2)
            m = 0-int(str2)
            if m >= -2**31 and m <= 2**31-1:
                return m
            else:
                return 0

s = Solution()
m = s.reverse(1534236469)
print(2**31-1)
print(m)

