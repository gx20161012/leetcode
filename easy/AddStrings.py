class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length1 = len(num1)
        length2 = len(num2)
        i = length1 - 1
        j = length2 - 1
        carry = 0
        string = ''
        while i >= 0 or j >= 0:
            if i < 0:
                a = 0
            else:
                a = int(num1[i])
            if j < 0:
                b = 0
            else:
                b = int(num2[j])
            sum = a + b + carry
            string += str(sum % 10)
            carry = sum // 10
            i -= 1
            j -= 1
        if carry == 1:
            string += '1'
        return string[::-1]

s = Solution()
print(s.addStrings("999", "999"))