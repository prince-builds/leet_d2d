# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack=[]
        c=root
        count=0
        while c or stack:
            while c:
                stack.append(c)
                c=c.left
            node=stack.pop()

            count+=1

            if count==k:
                return node.val
            c=node.right
        