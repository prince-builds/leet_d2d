class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        j=0
        c=0
        i=0

        while i< len(g) and j<len(s):
            if g[i]<=s[j]:
                c+=1
                i+=1
                j+=1
                
            else:
                j+=1

        return c

        