class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A=len(word1)
        B=len(word2)
        s=[]
        a=0
        b=0
        word=1
        while a<A and b<B:
            if word==1:
                s.append(word1[a])
                a+=1
                word=2
            else:
                s.append(word2[b])
                b+=1
                word=1
        while a<A:
            s.append(word1[a])
            a+=1
        while b<B:
            s.append(word2[b])
            b+=1
        return "".join(s)


        