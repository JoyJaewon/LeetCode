'''
input: list[int]
output: integer - maximum width of ramp. w = j - i

Clarifications
- there can be duplicate values
- every number will be greater than or equal to 0

'''
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0  
        stack = []

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width
