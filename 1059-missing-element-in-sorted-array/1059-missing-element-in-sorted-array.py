class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        first_val = nums[0]
        
        missing_total = nums[-1] - first_val - right
        if missing_total < k:
            return nums[-1] + (k - missing_total)

        while left < right:
            mid = (left + right) // 2
            missing = nums[mid] - first_val - mid
            
            if missing < k:
                left = mid + 1
            else:
                right = mid
        
        return nums[left - 1] + (k - (nums[left - 1] - first_val - (left - 1)))
