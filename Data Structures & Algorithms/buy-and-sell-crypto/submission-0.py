class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        for i in range(len(prices)):
            for x in prices[i:]:
                if x>prices[i]:
                    sell_price = x
                    cost_price = prices[i]
                    profit = sell_price - cost_price
                    max_profit = max(max_profit, profit)
        return max_profit