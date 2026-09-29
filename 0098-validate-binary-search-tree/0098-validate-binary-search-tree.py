# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def v(n,l,h):
            if n is None:
                return True
            if n.val <= l or n.val>=h:
                return False
            lv=v(n.left,l,n.val)
            rv=v(n.right,n.val,h)

            return lv and rv
        return v(root,float('-inf'), float('inf'))
        