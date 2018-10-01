class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        str1 = str(n)
        length = len(str1)
        sum  = 0
        list1 = list()
        for i in range(length):
            sum += int(str1[i]) ** 2
        while sum not in list1:
            if sum == 1:
                return True
            list1.append(sum)
            str2 = str(sum)
            sum = 0
            length1 = len(str2)
            for i in range(length1):
                sum += int(str2[i]) ** 2

        return False

s = Solution()
print(s.isHappy(11))