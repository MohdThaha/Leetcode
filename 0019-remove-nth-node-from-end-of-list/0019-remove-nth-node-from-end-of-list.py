# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def remove(node):
            if not node:
                return 0

            pos = remove(node.next) + 1

            if pos == n+1:
                node.next = node.next.next
            return pos

        pos = remove(head)

        if pos == n:
            return head.next

        return head           
           