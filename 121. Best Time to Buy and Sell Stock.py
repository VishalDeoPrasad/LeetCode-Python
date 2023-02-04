class Solution(object):

    #solve in o(n2)
    def maxProfit1(self, prices):
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit\

    def maxProfit(self, prices):
        min_so_far = prices[0]              #7
        max_profit = 0  
        curr_profit = 0                    #0
        for i in range(len(prices)):        
            #print(i, '-->', min_so_far, max_profit)
            if min_so_far > prices[i]:      #7-7
                min_so_far = prices[i]      

            curr_profit = prices[i] - min_so_far  #7-7=0
            #print(curr_profit)
            if max_profit < curr_profit:    
                max_profit = curr_profit
        return max_profit



prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))