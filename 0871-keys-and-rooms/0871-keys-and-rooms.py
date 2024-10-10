'''
input: 2D list
output: boolean - check if you can visit all the rooms

Test Cases
[[1],[2],[3],[]]
0->1->2->3 True

'''
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        queue = deque([0])
        visited[0] = True

        while queue:
            curr_v = queue.popleft()
            for next_v in rooms[curr_v]:
                if not visited[next_v]:
                    queue.append(next_v)
                    visited[next_v] = True
        
        return all(visited)
        