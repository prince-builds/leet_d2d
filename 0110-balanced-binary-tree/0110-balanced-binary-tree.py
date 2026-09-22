# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def h(node):
            if node is None:
                return 0
            hl=h(node.left)
            if hl==-1:
                return -1
            hr=h(node.right)
            if hr == -1:
                return -1
            if abs(hr-hl)>1:
                return -1
            return 1 + max(hl,hr)
        return h(root)!=-1
        