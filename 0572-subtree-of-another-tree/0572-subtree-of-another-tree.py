class Solution:

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True

        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        leftt = self.isSubtree(root.left, subRoot)
        rightt = self.isSubtree(root.right, subRoot)

        return leftt or rightt