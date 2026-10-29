class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxx=0
        for customer in accounts:
            maxx=max(maxx,sum(customer))
        return maxx
        