# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        node_list = []
        while node:
            node_list.append(ListNode(node.val))
            node = node.next

        len_list = len(node_list)
        ans = ListNode()
        prev = ans 
        
        for i in range(len_list):
            if i == (len_list - n):
                continue
            else:
                prev.next = node_list[i]
                prev = node_list[i]
        
        return ans.next