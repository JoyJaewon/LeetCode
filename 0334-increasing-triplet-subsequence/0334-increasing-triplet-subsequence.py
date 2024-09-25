'''
input: list 
output: boolean - true if there exists a triplet where nums[i] < nums[j] < nums[k]

Clarifications
- length of the list can be less than 3
- number can be negative
- there can be multiple valid cases
- triplet doesn't have to be next to each other

Test Cases
[1,2,3,4,5] -> true
[5,4,3,2,1] -> false
[1,2] -> false
[1,-1,2,-2,3] -> true (1,2,3)

Approach 1) use triple for-loop to check each combinations O(N^3)
Approach 2) use double for-loop + two pointer O(N^2)
Approach 3) 
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')  
        second = float('inf') 
        
        for num in nums:
            if num <= first:
                first = num  
            elif num <= second:
                second = num  
            else:
                return True
        
        return False

