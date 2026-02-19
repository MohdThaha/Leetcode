# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0 

        def dfs(node):

            nonlocal res

            if not node:
                return 

            if node.left and not node.left.left and not node.left.right:
                res += node.left.val

            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return res

        