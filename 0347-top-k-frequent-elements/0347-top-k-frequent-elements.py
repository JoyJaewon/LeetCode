'''
use dictionary to count the frequency
use heap to keep k most frequent elements

[1,1,1,2,2,3,5,6,7] -> {1:3, 2:2, 3:1, 5:1, 6:1, 7:1} k = 2 
'''
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        
        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [key for val, key in heap]
        