class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        pairs={ ")":"(", "]":"[", "}":"{" }
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()

                if top!=pairs[i]:
                    return False
        return not stack
        