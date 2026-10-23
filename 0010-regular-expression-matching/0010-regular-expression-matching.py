class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            # Base case: if pattern is exhausted, string must also be exhausted
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Case 1: The next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option A: Ignore '*' and its preceding element (0 occurrences)
                # Option B: Use '*' to match current s[i] (1+ occurrences), keeping pattern at j
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Case 2: Standard single-character transition
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)