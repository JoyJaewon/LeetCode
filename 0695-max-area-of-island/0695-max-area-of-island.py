class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_area = 0

        def isInRange(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def dfs(r,c):
            if not isInRange(r,c) or grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            count = 1
            for x, y in directions:
                nx, ny = r + x, c + y
                count += dfs(nx, ny)
            return count

        for r in range(row):
            for c in range(col):
                if not visited[r][c] and grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area