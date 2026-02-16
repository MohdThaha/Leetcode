class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # leaf node
        if not root.left and not root.right:
            return 1
        
        # if one side missing, ignore it
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # both exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
