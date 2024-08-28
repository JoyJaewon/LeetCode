'''
input: 2D array, integer k
output: 2D array - k closest points to the origin (0,0)

Approach)
relative distance can be calcualted by x**2 + y**2
go through the points, pushpop into the heap. maintain length of k

O(nlogn), O(n)
'''
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point
            dist = -(x ** 2 + y ** 2)

            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            else:
                heapq.heappushpop(heap, (dist, x, y))
        
        return [[x, y] for (dist, x,y) in heap]