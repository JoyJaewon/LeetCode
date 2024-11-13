'''
clarifications
- can have duplicate elements in the array

test cases
[1,1,1,2,2,3], k=2 => 1:3, 2:2, 3;1 => [1,2]

plan
- count the frequency  # key: element, value: count
- going through the dictionary with count
    - heap
    - 카운트 큰것만 킵

TC: O(nlogn), SC: O(N)
'''
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for key, values in count.items():
            heapq.heappush(heap, (values, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [value for _, value in heap]

        