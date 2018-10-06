class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dict1 = dict()
        for i in range(length):
            if s[i] in dict1.keys():
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1
        for i in range(length):
            if dict1[s[i]] == 1:
                return i
            else:
                continue
        return -1
s = Solution()
s1 = "loveleetcode"
print(s.firstUniqChar(s1))