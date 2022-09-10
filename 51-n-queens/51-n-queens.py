class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
   
        col_set = set()
        diag_set = set()
        anti_diag_set = set()
        
        result = []

        def backtrack(row, state):
            
            if row == n:
                result.append(create_board(state))
                return
            
            for col in range(n):
                
                diag = row - col
                antidiag = row + col
                
                if col in col_set or diag in diag_set or antidiag in anti_diag_set:
                    continue
                
                col_set.add(col)
                diag_set.add(diag)
                anti_diag_set.add(antidiag)
                state[row][col] = 'Q'
                
                backtrack(row + 1, state)
                
                col_set.remove(col)
                diag_set.remove(diag)
                anti_diag_set.remove(antidiag)
                state[row][col] = '.'
        
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        state = [['.'] * n for _ in range(n)]
        backtrack(0, state)
        return result