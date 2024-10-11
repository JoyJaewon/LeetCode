'''
input: list[int] - sorted, integer - target
output: list[int] - indices of two numbers, 1-based index

Test Cases
[2,7,11,15], 9 => [1,2]

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        result = []

        while left < right:
            num_sum = numbers[left] + numbers[right]

            if num_sum == target:
                return [left + 1, right + 1]

            if num_sum > target:
                right -= 1
            
            else: 
                left += 1
        
        return []
        