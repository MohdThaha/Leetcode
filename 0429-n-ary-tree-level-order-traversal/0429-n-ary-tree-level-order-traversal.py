"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)
            
            for child in node.children:
                dfs(child, level + 1)
        
        dfs(root, 0)
        return result