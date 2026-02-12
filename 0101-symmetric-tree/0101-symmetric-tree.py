# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        res = True

        def check(left, right):
            nonlocal res   

            if not left and not right:
                return
            
            if not left or not right:
                res = False
                return

            if left.val != right.val:
                res = False
                return
            
            
            check(left.left, right.right)
            check(left.right, right.left)

        check(root.left, root.right)   
        return res
        