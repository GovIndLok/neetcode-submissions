class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]

        profit = 0
        for curr in range(len(prices)):
            if prices[curr] < buy:
                buy = prices[curr]
            
            curr_profit = prices[curr] - buy
            profit = max(curr_profit, profit)
            
        return profit