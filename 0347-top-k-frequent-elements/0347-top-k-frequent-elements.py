from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [key for val, key in heap]
    
    # O(nlong), O(n)