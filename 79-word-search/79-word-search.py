class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        visited = set()
        
        def dfs(r,c,i):
        
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited:
                return False
            
            if i == len(word) - 1 and word[i] == board[r][c]:
                return True
            
            if word[i] != board[r][c]:
                return False
            
            visited.add((r,c))
            
            result = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1)
            )
            
            visited.remove((r,c))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False