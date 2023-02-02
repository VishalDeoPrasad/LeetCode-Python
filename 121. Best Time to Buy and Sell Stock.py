class Solution(object):

    #solve in o(n2)
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))