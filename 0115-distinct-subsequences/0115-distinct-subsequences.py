class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        # dp[j] stores the number of distinct subsequences of s[:i] that equal t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # An empty t can always be formed by 1 empty subsequence

        for char_s in s:
            # Iterate backwards to use values from the previous iteration of s
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
        