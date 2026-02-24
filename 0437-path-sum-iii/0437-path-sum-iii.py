# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, remaining):
            if not node:
                return 0
            
            count = 0
            if node.val == remaining:
                count += 1
            
            count += dfs(node.left, remaining - node.val)
            count += dfs(node.right, remaining - node.val)
            
            return count
        
        if not root:
            return 0
        
        return (
            dfs(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
        