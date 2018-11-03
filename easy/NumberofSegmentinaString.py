class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        count = 0
        i = 0
        while i < length:
            if s[i] == " ":
                i += 1
                continue
            count += 1
            while i < length and s[i] != " ":
                i += 1
        return count
s = Solution()
str = "Hello, my name is John"
print(s.countSegments(str))