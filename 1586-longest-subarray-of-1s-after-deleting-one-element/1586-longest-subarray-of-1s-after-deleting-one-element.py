'''
input - list[int]
output: integer - longest size of subarray containing only 1s

Clarification
- we SHOULD delete 1 element
- minimum length of the list will be 1
- the list will contain only 0s and 1s

Test Cases
[1,1,0,1] => 3
[0,0,0] => 0
[1,1,1] => 2

Approach 1) Brute Force - check all the possibilities O(N^2)
Approach 2) Sliding Window - O(N)

Plan
- define the function taking the list as parameter
    - initialize longest to 0
    - initialize zero_count to 0
    - initialize left pointer to 0
    - iterate over the list using the right pointer
        - if the current element is zero, update zero_count
        - while zero_count > 1
            - if list[left] == 0
                - zero_count -= 1
            - move left pointer += 1
        - update the longest
    - return longest

TC: O(N), SC: O(1)
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        zero_count = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            longest = max(longest, right - left)
        
        return longest
        