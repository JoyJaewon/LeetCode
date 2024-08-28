'''
5th largest
python heapify - min heap
[3,2,1,5,6,4] => [-6, -5, -4, -3, -2, -1], k = 2


'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)
        
        return -nums[0] 
        