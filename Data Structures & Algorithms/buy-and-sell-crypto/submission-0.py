class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, len(prices) - 1
        profit = 0

        while i < j:
            for k in range(i+1, j+1):
                if prices[k] >= prices[j]: j = k
            for k in range(i, j):
                if prices[k] <= prices[i]: i = k
            profit = max(profit, prices[j] - prices[i])
            i, j = j + 1, len(prices) - 1
        return profit
            
