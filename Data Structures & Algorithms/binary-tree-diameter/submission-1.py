# Definition for a binary tree node.
# class TreeNode:
from types import resolve_bases
#     def __init__(AnyStr, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def traverse(node):
            if not node:
                return 0
            
            left = traverse(node.left) 
            right = traverse(node.right)

            self.ans = max(self.ans, left + right )
            return 1 + max(left, right)
        
        traverse(root)
        return self.ans