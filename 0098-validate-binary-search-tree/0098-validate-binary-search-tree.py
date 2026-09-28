class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            left_valid = validate(node.left, low, node.val)
            right_valid = validate(node.right, node.val, high)

            return left_valid and right_valid

        return validate(root, float('-inf'), float('inf'))