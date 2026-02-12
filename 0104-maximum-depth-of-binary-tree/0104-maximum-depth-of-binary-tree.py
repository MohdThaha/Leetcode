# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node,level):
            nonlocal res
            if not node:
                res = max(res,level)
                return
            depth(node.left,level+1)
            depth(node.right,level+1)
        depth(root,0)
        return res
            

        