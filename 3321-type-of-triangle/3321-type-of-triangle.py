'''
input: list[int]
output: string - check what type of triangle it can form

Clarifications
- there will be 3 integers given
- length of longest <= sum of 2 other sides

Test Cases
[1,1,1] -> equilateral
[2,2,3] -> isosceles
[1,2,3] -> scalene
[3,1,1] -> None (1+1 !>= 3)

Approach) find the longest, store the value. if not longest <= sum of 2 other side, return -1, then go through each cases

Plan
- define the function taking the list as a parameter
    - initialize the longest = max(nums)
    - initialize other two variables
    - if not longest <= sum of 2 other sides, return -1
    - go through each case

TC: O(N), SC: O(1)
'''
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        longest = max(nums)
        nums.remove(longest)
        num1, num2 = nums
        
        if longest >= num1 + num2:
            return "none"
        
        if longest == num1 == num2:
            return "equilateral"
        elif longest == num1 or num1 == num2 or longest == num2:
            return "isosceles"
        else:
            return "scalene"
        