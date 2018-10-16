class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        list1 = list()
        while n != 0:
            if n % 26 == 0:
                list1.append('Z')
                n = n // 26 - 1
            else:
                list1.append(chr(n % 26 + 64))
                n = n // 26
        str1 = ''
        for i in list1[::-1]:
            str1 = str1 + i
        return str1
s = Solution()
print(s.convertToTitle(701))