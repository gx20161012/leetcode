class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s = dict()
        for i in range(len(s)):
            if s[i] not in dict_s.keys():
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1
        print(dict_s)
        length = 0
        flag = False
        for key in dict_s.keys():
            print(key)
            if dict_s[key] % 2 == 0:
                length += dict_s[key]
            elif dict_s[key] == 1:
                flag = True
            else:
                flag = True
                length += dict_s[key] - 1
        if flag == True:
            return length + 1
        else:
            return length

s = Solution()
string = "ababababa"
print(s.longestPalindrome(string))