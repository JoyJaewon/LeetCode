'''
input: list, inter k
output: integer - kth largest element in the array

Clarification
- can there be duplicate numbers in the list? yes
- can there be negative numbers in the list? yes
- do we count duplicate numbers when considering the largest element? yes

Test Cases
[3,2,1,5,6,4], 2 -> 5
[6,5,5,4,3], 3 -> 5

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num - min_val] += 1
        
        remain = k
        for num in range(len(count) -1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_val
