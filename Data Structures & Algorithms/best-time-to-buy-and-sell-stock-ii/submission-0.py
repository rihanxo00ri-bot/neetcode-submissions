class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_sell=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit=prices[i+1]-prices[i]
                max_sell +=profit

             
 
        return max_sell            