class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = list()
        max = 0
        for char in s:
            if char not in list_s:
                list_s.append(char)
                if max < len(list_s):
                    max = len(list_s)
            else:
                if list_s.index(char) == len(list_s):
                    list_s = []
                    list_s.append(char)
                else:
                    list_s = list_s[list_s.index(char)+1:len(list_s)]
                    list_s.append(char)
        return max
s = Solution()
string = 'abcabcbb'
print(s.lengthOfLongestSubstring(string))