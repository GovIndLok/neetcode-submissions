class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = prices[0]
        buy = prices[0]

        profit = 0
        for curr in range(len(prices)):
            if prices[curr] > sell:
                sell = prices[curr]

            if prices[curr] < buy:
                buy = prices[curr]
                sell = prices[curr]

            curr_profit = sell - buy
            if curr_profit > profit:
                profit = curr_profit
            
        return profit