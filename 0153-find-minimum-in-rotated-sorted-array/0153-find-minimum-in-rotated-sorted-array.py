'''
[4,5,6,7,0,1,2]
l
            r
mid = (l + r) // 2 = 0 + 6 // 2 = 3 , nums[mid] = 7
- check if nums[mid] > nums[right] 
    - if yes, that means minimum is in the right side.
        - left = mid + 1
    - if no, that means, minimum is in the left side
        - right = mid - 1



'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]