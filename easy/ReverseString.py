class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        return r
s = Solution()
str1 = "hello"
print(s.reverseString(str1))