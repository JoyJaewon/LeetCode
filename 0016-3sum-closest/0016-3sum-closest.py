class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                num_sum = nums[i] + nums[left] + nums[right]

                if num_sum == target:
                    return num_sum

                diff = abs(target - num_sum)
                if abs(target - result) > diff:
                    result = num_sum
                
                if num_sum > target:
                    right -= 1
                    
                else: 
                    left += 1
        
        return result
