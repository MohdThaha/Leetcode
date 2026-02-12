# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        def bfs(node,level):
            if not node:
                return
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)

            bfs(node.left,level+1)
            bfs(node.right,level+1)
        bfs(root,0)

        return result[::-1]

            
        