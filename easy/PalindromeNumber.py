class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length-1-i]:
                return False
            else:
                continue
        return True
s = Solution()
print(s.isPalindrome(122))
