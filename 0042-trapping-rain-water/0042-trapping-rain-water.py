class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_max, right_max = height[0], height[-1]
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
        