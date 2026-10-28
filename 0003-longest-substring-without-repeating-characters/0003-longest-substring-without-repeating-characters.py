class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        seen=set()
        l=0
        maxx=0
        for r in range (n):

        
            while s[r]in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])

            c=r-l+1

            maxx=max(c,maxx)
        return maxx