# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.count = 0
        
        def dfs(node, currSum):
            if not node:
                return
            
            currSum += node.val
            
            self.count += prefix[currSum - targetSum]
            
            prefix[currSum] += 1
            
            dfs(node.left, currSum)
            dfs(node.right, currSum)
            
            prefix[currSum] -= 1  # backtrack
        
        dfs(root, 0)
        return self.count
        