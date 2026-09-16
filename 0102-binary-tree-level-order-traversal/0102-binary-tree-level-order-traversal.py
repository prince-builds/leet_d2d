# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        q=[]
        r=[]
        q.append(root)
        while q:
            ln=len(q)
            l=[]
            for _ in range(ln):
                node=q.pop(0)
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            r.append(l)
        return r
        