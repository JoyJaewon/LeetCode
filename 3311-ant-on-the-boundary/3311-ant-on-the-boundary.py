'''
input: list[int]
output: integer - number of times the ant returns to the boundary

Clarifications
- if the ant reaches the boundary,it counts.
- but if the ants pass the boundary, it doens't count
- boundary is 0

Test Cases
[2,3,-5] => 1
[3,2,-3,-4] => 0
'''
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        curr = 0

        for num in nums:
            curr += num
            if curr == 0:
                count += 1
        
        return count
        