class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def helper(l, r):
            if l > r:
                return None 
            #this is the base case to ensure the pointer moves in the right direction

            m = (l + r ) // 2
            #the midpoint 
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            #this creates the tree branches using the midpoint pointer as the nodes 
            return root

        return helper(0, len(nums) - 1)