class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        minn=prices[0]
        maxx=0
        for i in range(n):
            if prices[i]<minn:
                minn=prices[i]

            profit=prices[i]-minn
            maxx=max(maxx,profit)
        return maxx
        