# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        q = head
        while q is not None and q.next is not None:
            s = s.next
            q = q.next.next

            if s == q:
                return True

        return False
        