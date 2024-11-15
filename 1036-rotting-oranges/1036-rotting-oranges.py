'''
- input: 2d array 0: empty 1: fresh 2: rotten
- output: integer - min num of minutes for all the oranges become rotten

Clarifications
- only 0, 1, 2 acceptable
- what if the grid was empty? return 0
- what if the grid given is already full with rotten oranges? return 0

[
    [2,2,2]
    [2,2,0]
    [0,2,2]
    4
]
Approach) using BFS and travel by level. 

Plan
- bfs
    - initialization
        - go through the grid, and find the rotten oranges and put them into the queue
        - count the number of fresh oranges
    - while # of fresh orange > 0 and while queue
        - for _ in range(len(queue)):
            pop
            check up down left right 
                if fresh, add it to queue, convert that into Rotten
        - time + 1
    return time if the number of fresh == 0 else -1
TC: o(n*m) SC: o(n*m)

'''
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time = 0
        fresh = 0
        ROTTEN, EMPTY, FRESH = 2, 0, 1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == ROTTEN:
                    queue.append((r, c))
                elif grid[r][c] == FRESH:
                    fresh += 1

        def isInRange(r,c):
            return 0 <= r < len(grid) and 0 <= c< len(grid[0])

        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for x, y in directions:
                    nx, ny = x + r, y + c
                    if isInRange(nx, ny) and grid[nx][ny] == FRESH:
                        queue.append((nx, ny))
                        grid[nx][ny] = ROTTEN
                        fresh -= 1
            time += 1
        
        return -1 if fresh else time


        