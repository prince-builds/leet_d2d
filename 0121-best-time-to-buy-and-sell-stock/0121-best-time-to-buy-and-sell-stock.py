class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        minp=prices[0]
        maxp=0
       
        for i in range(n):
            if prices[i]<minp:
                minp=prices[i]
            
            profit=prices[i]-minp

            if profit>maxp:
                maxp=profit
        return maxp