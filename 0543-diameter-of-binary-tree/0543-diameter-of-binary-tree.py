class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.d = 0

        def h(node):
            if node is None:
                return 0

            lh = h(node.left)
            rh = h(node.right)

            self.d = max(self.d, lh + rh)

            return 1 + max(lh, rh)

        h(root)

        return self.d