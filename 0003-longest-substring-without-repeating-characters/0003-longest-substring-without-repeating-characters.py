class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=0
        maxx=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[right])
       
            c=right-l+1

            maxx=max(maxx,c)
        return maxx
        