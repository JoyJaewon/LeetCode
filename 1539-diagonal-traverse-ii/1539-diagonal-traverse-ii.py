'''
input - 2D list
output - list

Clarification
- given 2D list is not always perfect n * m (can have empty spots)

'''
from collections import deque
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0,0)])
        result = []

        while queue:
            row, col = queue.popleft()
            result.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))
            
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
        
        return result

        
        