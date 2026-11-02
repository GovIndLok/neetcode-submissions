# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        two = slow.next
        slow.next = None
        prev = None
        while two:
            tmp = two.next
            two.next = prev
            prev = two
            two = tmp
        
        alpha, beta = head, prev
        while beta:
            tmp1, tmp2 = alpha.next, beta.next
            alpha.next = beta
            beta.next = tmp1
            alpha = tmp1
            beta = tmp2