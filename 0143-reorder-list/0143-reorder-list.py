# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        nodes = []
        curr = head
        
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        l, r = 0, len(nodes) - 1
        
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            
            if l > r:
                break
                
            nodes[r].next = nodes[l]
            r -= 1
        
        nodes[l].next = None
