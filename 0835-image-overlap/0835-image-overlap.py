class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Collect coordinates of all 1s
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count frequency of each translation vector (dr, dc)
        shift_counts = defaultdict(int)
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_counts[(r2 - r1, c2 - c1)] += 1
                
        return max(shift_counts.values()) if shift_counts else 0
        