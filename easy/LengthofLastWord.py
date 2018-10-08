class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.split(' ')
        length = len(s_list)
        for i in range(length):
            if s_list[length-1-i] != '':
                return len(s_list[length-1-i])
            else:
                continue
        return 0
s = Solution()
st = "     "
print(s.lengthOfLastWord(st))