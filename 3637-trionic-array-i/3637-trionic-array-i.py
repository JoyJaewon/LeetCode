'''
input: array 
output: boolean - check if the array is trionic

[1,3,5,4,2,6,1]
     p
         q
           r
              
1->3->5 
5->4->2
2->6
=> trionic

- iterate over the array
    - while
      - increase
    - p = curr
    - while
        - decrease
    - q = curr
    - while
        - increase
    - r = curr
    - return p > 0 and p > q and q < n - 1 and r = n - 1

TC: O(N), SC: O(1)
    
'''
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]: # increase
            i += 1
        p = i

        while i + 1 < n and nums[i] > nums[i + 1]: # decrease
            i += 1
        q = i

        while i + 1 < n and nums[i] < nums[i + 1]: # increase
            i += 1
        
        return p > 0 and q > p and q < n - 1 and i == n - 1

        