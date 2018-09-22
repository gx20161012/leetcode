"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        maxprofit = 0
        for i in range(1, length, 1):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                maxprofit += diff
        return maxprofit

s = Solution()
prices = [7, 1, 5, 3, 6, 4]
max = s.maxProfit(prices)
print(max)