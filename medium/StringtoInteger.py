class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        string = ""
        str = str.lstrip(" ")
        if str == '':
            return 0
        length = len(str)
        if str[0].isdigit() == False:
            if str[0] == '-' or str[0] == '+':
                string += str[0]
            else:
                return 0
        else:
            string += str[0]
        for i in range(1, length):
            if str[i].isdigit() == True:
                string += str[i]
            else:
                break
        if string == '-' or string == '+':
            return 0
        else:
            if int(string) < -(2**31):
                return -(2**31)
            elif int(string) > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(string)

s = Solution()
string = '+91283472332'
print(s.myAtoi(string))