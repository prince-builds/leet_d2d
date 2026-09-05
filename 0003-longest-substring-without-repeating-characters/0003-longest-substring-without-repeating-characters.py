class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        seen=set()
        left=0
        max_length=0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            c=right-left+1
            max_length=max(max_length,c)
        return max_length