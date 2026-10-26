class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root = TreeNode(root1.val + root2.val)

        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root
    


