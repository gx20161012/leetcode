"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 0 or length == 1:
            return True
        s = s.lower()
        list1 = list()
        for i in range(length):
            if str(s[i]).isalnum():
                list1.append(s[i])
        
        l = len(list1)
        if l == 0 or l == 1:
            return True
        flag = False
        for j in range(l):
            if list1[j] != list1[l - 1 - j]:
                return False
            else:
                flag = True
                continue
        return flag


s = Solution()
flag = s.isPalindrome("")
print(flag)
        