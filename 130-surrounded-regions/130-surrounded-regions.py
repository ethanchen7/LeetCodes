class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # board cell is only NOT valid if it's on the edge
        rows = len(board)
        cols = len(board[0])
        
        def capture(r,c): # capture all the cells coming from the edge
            
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
            
        # start from the border and capture all cells that connect with the border
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1] and board[r][c] == "O":
                    capture(r, c)
        
        # mark all the surrounded regions with Xs, because these are for sure not connected to the borders
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # unmark the borders back to "O" instead of "T"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        