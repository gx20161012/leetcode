class Solution:
    def countStr(self,s):
        count = 0
        ans = ''
        temp = s[0]
        for i in range(len(s)):
            if temp == s[i]:
                count = count + 1
            else:
                ans = ans + str(count) + temp
                temp = s[i]
                count = 1
        ans = ans + str(count) + temp
        return ans
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        while n > 1:
            ans = self.countStr(ans)
            n = n - 1
        return ans

s = Solution()
for i in range(1, 30, 1):
    ans = s.countAndSay(i)
    print(ans)