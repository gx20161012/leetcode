class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        for i in range(len(str(bin(z)))):
            if str(bin(z))[i] == '1':
                count += 1
        return count

s = Solution()
print(s.hammingDistance(1, 4))