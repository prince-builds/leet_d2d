class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        n=len(s)
        l=0
        mm=0
        for right in range (n):
            while s[right] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[right])

            c=1+right-l

            mm=max(mm,c)
        return mm

        