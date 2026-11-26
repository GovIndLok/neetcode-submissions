"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_list = {None: None}

        curr = head
        while curr:
            ans = Node(curr.val)
            node_list[curr] = ans
            curr = curr.next

        curr = head
        while curr:
            ans = node_list[curr]
            ans.next = node_list[curr.next]
            ans.random = node_list[curr.random]
            curr = curr.next
        
        return node_list[head]