# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d=0
        def h(n):
            if not n:
                return 0
            lh=h(n.left)
            rh=h(n.right)

            self.d=max(self.d,rh+lh)
            return 1 + max(lh,rh)

        h(root)
        
        return self.d