class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_left
from typing import List


class Solution:

  def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
    # Store intervals as (r, l, weight, original_index) and sort by right boundary r
    events = sorted(
        [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)],
        key=lambda x: x[0],
    )
    n = len(events)
    ends = [e[0] for e in events]

    # dp[i][j] = (-max_weight, [sorted_indices]) considering a prefix of first i intervals and choosing j intervals
    # We store -weight so Python's min() naturally maximizes weight,
    # and breaks ties by lexicographically smallest index list.
    dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

    for i, (r, l, weight, orig_idx) in enumerate(events):
      # Find largest index k such that ends[k] < l
      # bisect_left(ends, l) gives first index where ends >= l, which is the exact count of valid non-overlapping intervals
      k = bisect_left(ends, l, 0, i)

      for j in range(1, 5):
        # Option 1: Skip the current interval
        best = dp[i][j]

        # Option 2: Take the current interval
        prev_weight, prev_indices = dp[k][j - 1]
        take_weight = prev_weight - weight
        take_indices = sorted(prev_indices + [orig_idx])
        take = (take_weight, take_indices)

        # min selects greater weight first, then lexicographically smaller indices
        dp[i + 1][j] = min(best, take)

    # Find the best combination among choosing 1, 2, 3, or 4 intervals
    best_overall = min(dp[n][1:])
    return best_overall[1]
        