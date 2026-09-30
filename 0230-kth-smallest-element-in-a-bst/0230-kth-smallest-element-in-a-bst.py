# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        s=[]
        cu=root
        c=0
        while cu or s:
            while cu:
                s.append(cu)
                cu=cu.left
            node=s.pop()
            c+=1

            if c==k:
                return node.val
            cu=node.right