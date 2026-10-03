class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxx=0
        for i in accounts:
           m=sum(i)
           maxx=max(maxx,m)
        return maxx