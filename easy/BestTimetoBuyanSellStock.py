#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
#design an algorithm to find the maximum profit.
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        dp = [0]
        minprice = prices[0]
        for i in range(1, length, 1):
            minprice = min(minprice, prices[i])
            dp.append(max(dp[i-1], prices[i] - minprice))
        return dp[length-1]



s = Solution()
prices = [7, 1, 5, 3, 6, 4]
max = s.maxProfit(prices)
print(max)