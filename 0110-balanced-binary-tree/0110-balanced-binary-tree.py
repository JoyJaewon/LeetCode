# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def dfs(node):
            nonlocal is_balanced
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                is_balanced = False

            return max(left, right) + 1
        
        dfs(root)
        return is_balanced

        