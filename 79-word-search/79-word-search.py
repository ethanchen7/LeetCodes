class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def dfs(r,c,i):
            
            if i == len(word): return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            if (r,c) in visited:
                return False
            
            if word[i] != board[r][c]:
                return False
            
            visited.add((r,c))
            result = (dfs(r - 1, c, i + 1) or 
                    dfs(r + 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))
            
            if result: return True
            
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and (r,c) not in visited:
                    res = dfs(r, c, 0)
                    if res:
                        return True
        
        return False
            