# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def traverse(node, ans):
            if not node:
                return ans
            
            return max(traverse(node.left, ans + 1), traverse(node.right, ans + 1))
        
        return traverse(root, res)