class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        seen=set()
        l=0
        m=0
        for right in range (n):
            while s[right] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[right])
            c=1+right-l
            m=max(m,c)
        return m


        