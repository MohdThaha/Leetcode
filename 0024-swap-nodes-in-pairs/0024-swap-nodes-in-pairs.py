# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            temp = second.next

            prev.next = second
            second.next = first
            first.next = temp

            prev = first

        return dummy.next
