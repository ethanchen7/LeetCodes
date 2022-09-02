class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        columns = set()
        diagonals = set()
        anti_diagonals = set()
        
        result = []
        
        def create_board(state):
            
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        def backtrack(row, state):
            
            if row == n:
                result.append(create_board(state))
                return
            
            for col in range(n):
                current_diagonal = row - col
                current_anti_diagonal = row + col
                
                if (col in columns or current_diagonal in diagonals or current_anti_diagonal in anti_diagonals):
                    continue
                
                columns.add(col)
                diagonals.add(current_diagonal)
                anti_diagonals.add(current_anti_diagonal)
                state[row][col] = 'Q'
                
                backtrack(row + 1, state)
                
                columns.remove(col)
                diagonals.remove(current_diagonal)
                anti_diagonals.remove(current_anti_diagonal)
                state[row][col] = '.'
            
        state = [['.'] * n for _ in range(n)]
        backtrack(0, state)
        return result