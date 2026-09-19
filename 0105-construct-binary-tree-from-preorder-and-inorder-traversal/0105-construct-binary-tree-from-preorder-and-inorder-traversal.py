# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        root_val=preorder[0]
        root=TreeNode(root_val)

        idx=inorder.index(root_val)
        left_inorder=inorder[:idx]
        right_inorder=inorder[idx+1:]

        left_preorder=preorder[1:idx+1]
        right_preorder=preorder[idx+1:]

        root.left=self.buildTree(left_preorder,left_inorder)
        root.right=self.buildTree(right_preorder,right_inorder)
        
        return root