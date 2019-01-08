class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if prices:
            length = len(prices)
            for i in range(length-1):
                if prices[i] < prices[i+1]:
                    res += prices[i+1] - prices[i]
        return res
prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))