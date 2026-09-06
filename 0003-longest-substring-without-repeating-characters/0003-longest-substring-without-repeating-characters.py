class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        seen=set()
        left=0
      
        max_lenght=0
        for right in range(n):
            while s[right]in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            
            c=right-left+1
            max_lenght=max(max_lenght,c)
        return max_lenght
        