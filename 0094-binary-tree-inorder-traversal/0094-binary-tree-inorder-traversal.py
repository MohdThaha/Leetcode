# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)        # 1️⃣ Traverse left
            result.append(node.val)  # 2️⃣ Visit root
            dfs(node.right)       # 3️⃣ Traverse right
        
        dfs(root)
        return result
        