# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def averageOfSubtree(self, root: TreeNode) -> int:
    count = 0

    def postorder(node):
      nonlocal count
      if not node:
        return 0, 0  # (subtree_sum, subtree_count)

      left_sum, left_cnt = postorder(node.left)
      right_sum, right_cnt = postorder(node.right)

      total_sum = left_sum + right_sum + node.val
      total_cnt = left_cnt + right_cnt + 1

      if node.val == total_sum // total_cnt:
        count += 1

      return total_sum, total_cnt

    postorder(root)
    return count