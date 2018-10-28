class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in range(len(t)):
            if t.count(t[i]) > s.count(t[i]):
                return t[i]
s = Solution()
s1 = "abcd"
t = "abcde"
print(s.findTheDifference(s1, t))