class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        p = 0
        list.sort(g)
        list.sort(s)
        for i in range(len(s)):
            if s[i] >= g[p]:
                res += 1
                p += 1
                if p >= len(g):
                    break
        return res
s = Solution()
g1 = [2,1,3]
s1 = [1,3,4,2]
print(s.findContentChildren(g1, s1))