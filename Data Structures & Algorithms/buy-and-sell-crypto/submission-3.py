class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #max_profit = 0
        #for i in range(len(prices)):
        #    for j in range(i, len(prices)):
        #        max_profit = max(prices[j] - prices[i], max_profit)
        #
        #return max_profit

        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(prices[r] - prices[l], max_profit)
            else:
                l = r
            r += 1
        return max_profit
