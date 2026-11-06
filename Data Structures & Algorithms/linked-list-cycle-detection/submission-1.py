# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        for i in range(2):
            if fast is None:
                return False

            fast = fast.next

        while fast:
            if fast == slow:
                return True
            
            tmp = fast.next
            fast = tmp.next if tmp is not None else None
            slow = slow.next
            
        return False