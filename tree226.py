class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        
        temp = root.left
        root.left = root. right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left) 
         
        return root