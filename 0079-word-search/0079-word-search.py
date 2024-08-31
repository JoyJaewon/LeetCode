class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[False]  * col for _ in range(row)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def isInRange(r,c):
            return 0 <= r < row and 0 <= c < col
                
        def backtrack(r, c, w):
            if not isInRange(r,c) or visited[r][c] or word[w] != board[r][c]:
                return False
            if w == len(word) - 1:
                return True
            
            visited[r][c] = True
            for x, y in directions:
                nx, ny = r + x, c + y
                if backtrack(nx, ny, w + 1):
                    return True
            visited[r][c] = False
            return False

        
        for r in range(row):
            for c in range(col):
                if backtrack(r, c, 0):
                    return True
        
        return False