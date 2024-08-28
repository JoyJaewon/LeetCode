from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row, col = len(rooms), len(rooms[0])
        queue = deque()
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        Inifnity = 2147483647

        def isInRange(r,c):
            return 0 <= r < row and 0 <= c < col 
        
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()
            for x, y in directions:
                nx, ny = r + x, c + y
                if isInRange(nx, ny) and rooms[nx][ny] == Inifnity:
                    rooms[nx][ny] = rooms[r][c] + 1
                    queue.append((nx, ny))