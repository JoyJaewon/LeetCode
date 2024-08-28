'''
input: 2D array with (u,v,w) u -> v, integer n, integer k
output: integer - minimum time it takes for all the n nodes to receive the signal from k
그래프 구성
pq 사용. 시작점을 넣음
curr_v 부터 neighbor를 방문하는데, 
'''
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        costs = {}
        pq = []
        graph = [[] for _ in range(n + 1)]
        
        for u, v, w in times:
            graph[u].append((w, v))
        
        heapq.heappush(pq, (0, k))
        
        while pq:
            curr_cost, curr_v = heapq.heappop(pq)
            if curr_v not in costs:
                costs[curr_v] = curr_cost
                for cost, next_v in graph[curr_v]:
                    if next_v not in costs:
                        next_cost = curr_cost + cost
                        heapq.heappush(pq, (next_cost, next_v))
            
        if len(costs) == n:
            return max(costs.values())

        return -1




        