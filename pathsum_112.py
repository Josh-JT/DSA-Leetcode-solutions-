class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return targetSum == curSum
            
            return (dfs(node.left, curSum) or dfs(node.right, curSum))

        return dfs(root, 0)