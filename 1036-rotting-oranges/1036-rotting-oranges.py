from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        time = 0
        fresh = 0
        queue = deque()

        def isInRange(r,c):
            return 0 <= r < row and 0 <= c < col

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for x, y in directions:
                    nx, ny = r + x, c + y

                    if isInRange(nx, ny) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1
       