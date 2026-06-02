'''
- if the length of the array is less than 2, return 0
- TC/SC O(N)

[1,6,3,9,2] -> [1,2,3,6,9] -> 1,1,3,3 => 3

Approach 1)
sort the array -> check the difference -> return the max => O(nlogn)

Approach 2)
counting / radix / bucket ? 



'''
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
'''



class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()

        max_num = 0 

        for i in range(1, len(nums)):
            max_num = max(max_num, nums[i] - nums[i - 1])
        
        return max_num     # TC: O(nlogn), SC: O(1)
