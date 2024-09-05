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

Approach) use heap 
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
        