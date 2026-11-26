# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        prevgroup = start
        while True:
            kth = self.getkth(prevgroup, k)
            if not kth:
                break
            nxtgroup = kth.next

            prev, curr = kth.next, prevgroup.next
            while curr != nxtgroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp 

            tmp = prevgroup.next
            prevgroup.next = kth
            prevgroup = tmp
        
        return start.next
    
    def getkth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr