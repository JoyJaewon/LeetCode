class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        number_of_islands = 0

        def isInRange(r,c):
            return 0 <= r < row and 0 <= c < col
        
        def dfs(r, c):
            if not isInRange(r,c) or visited[r][c] or grid[r][c] == '0':
                return
            visited[r][c] = True
            for x, y in directions:
                nx, ny = x + r, y + c
                dfs(nx, ny)
                
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r,c)
                    number_of_islands += 1
        
        return number_of_islands