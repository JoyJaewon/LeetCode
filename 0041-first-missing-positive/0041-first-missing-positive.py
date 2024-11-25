'''
TC O(N), SC O(1)

[1,2,0] => 3
[3,4,-1,1] => 2

'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 1

        for num in num_set:
            while ans in num_set:
                ans += 1

        return ans
        