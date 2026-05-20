class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  BruteForce
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         curr = prices[j]-prices[i]
        #         if(curr > max_profit):
        #             max_profit = curr
        # return max_profit

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit