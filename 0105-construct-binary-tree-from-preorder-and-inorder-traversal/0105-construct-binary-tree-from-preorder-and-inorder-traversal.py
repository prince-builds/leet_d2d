# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        root_val=preorder[0]
        root=TreeNode(root_val)

        idx=inorder.index(root_val)

        lo=inorder[ :idx]
        ro=inorder[idx+1:]

        lp=preorder[1:idx+1]
        rp=preorder[idx+1:]

        root.left=self.buildTree(lp,lo)
        root.right=self.buildTree(rp,ro)

        return root
        