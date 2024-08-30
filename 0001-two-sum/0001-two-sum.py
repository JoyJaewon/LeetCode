class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {} # diff, i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [i, num_dict[diff]]
            num_dict[num] = i
        
        return False
        