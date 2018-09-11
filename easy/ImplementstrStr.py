#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        if length == 0:
            return 0
        index = len(haystack)-length+1
        for i in range(int(index)):
            if haystack[i:i+length] == needle:
                return i
        
        return -1

s = Solution()
i = s.strStr("aaa", "a")
print(i)