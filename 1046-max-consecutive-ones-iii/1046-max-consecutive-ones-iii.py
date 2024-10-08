'''
input: list[int], integer k 
output: integer - maximum number of consecutive 1s with most k 0's

Clarifications
- k will be less than or equal to the length of the list
- the list will only contain 0s and 1s

Test Cases
[1,1,1,0,0,0,1], 2 => 5
[1,1,1,1,1], 2 => 5
[0,0,0,0,0], 5 => 5

Approach 1) Brute Force - check all the possibilities for every element. O(N^2)
Approach 2) sliding window, one pass. O(N)

Plan
- define the function taking the list and integer k as parameters
    - initialize max_count to 0 => this will count the maximum consecutive 1s
    - initialize zero_count to 0 
    - initialize left pointer to 0
    - iterate over the array using right pointer
        - if the current element is zero, update zero_count
        - while zero_count > k
            - decrease the left pointer
            - update zero_count
        - update max_count
    - return max_count
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        zero_count = 0
        left = 0    

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_count = max(max_count, right - left + 1)
            
        return max_count
        