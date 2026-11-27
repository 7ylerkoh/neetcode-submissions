class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j]
        #         profit = max(profit, sell - buy)
        # return profit

        # maxProfit = 0
        # left, right = 0, 1
        # while right < len(prices):
        #     buy = prices[left]
        #     sell = prices[right]
        #     if buy < sell:
        #         profit = sell - buy
        #         maxProfit = max(maxProfit, profit)
        #     else:
        #         left = right
        #     right += 1
        # return maxProfit

        maxProfit = 0
        minBuy = prices[0]
        for price in prices:
            maxProfit = max(maxProfit, price - minBuy)
            minBuy = min(minBuy, price)
        return maxProfit

