from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        row, col = len(maze), len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque([start])
        visited = set()

        def isInRange(r, c):
            return 0 <= r < row and 0 <= c < col

        while queue:
            r, c = queue.popleft()

            if [r, c] == destination:
                return True

            for x, y in directions:
                nr, nc = r, c
                
                while isInRange(nr + x, nc + y) and maze[nr + x][nc + y] == 0:
                    nr += x
                    nc += y

                if (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        return False  
