#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cs = [1, 1]
        for i in range(2, n+1, 1):
            cs.append(cs[i-1] + cs[i-2])
        return cs[n]

s = Solution()
print(s.climbStairs(6))