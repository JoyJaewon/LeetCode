from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        start_color = image[sr][sc]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        queue.append((sr, sc))

        if start_color == color:
            return image

        def isInRange(r,c):
            return 0 <= r < row and 0 <= c < col
        
        while queue:
            r, c = queue.popleft()
            image[r][c] = color

            for x, y in directions:
                nx, ny = r + x, c + y
                if isInRange(nx, ny) and image[nx][ny] == start_color:
                    queue.append((nx, ny))
        
        return image

# O(N*M), O(N*M)