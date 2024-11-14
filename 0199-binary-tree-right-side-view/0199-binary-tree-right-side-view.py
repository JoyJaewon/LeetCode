# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            rightSide = None
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                rightSide = curr_node.val
                if curr_node.left:
                    queue.append((curr_node.left))
                if curr_node.right:
                    queue.append((curr_node.right))
            result.append(rightSide)
        return result
        