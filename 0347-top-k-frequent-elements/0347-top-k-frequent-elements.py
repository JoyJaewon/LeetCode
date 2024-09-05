import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # {num, frequency}
        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [key for val, key in heap]

        