class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row_sets = [set() for i in range(9)]
        col_sets = [set() for j in range(9)]
        box_sets = [set() for z in range(9)]
        
        # populate the initial state
        for r in range(9):
            for c in range(9):
                
                if board[r][c] == '.':
                    continue
                
                value = int(board[r][c])
                
                row_sets[r].add(value)
                col_sets[c].add(value)
                
                box_idx = r // 3 * 3 + c // 3
                box_sets[box_idx].add(value)
        
        solved = False
        def backtrack(r, c):
            
            nonlocal solved
            
            if r == 9:
                solved = True
                return
            
            newR = r + (c + 1) // 9 # once we reach the end of the column, go down one row
            newC = (c + 1) % 9
            
            if board[r][c] != '.':
                backtrack(newR, newC)
            
            else:
                for num in range(1, 10):
                    box_idx = r // 3 * 3 + c // 3
                    if num not in row_sets[r] and num not in col_sets[c] and num not in box_sets[box_idx]:
                        row_sets[r].add(num)
                        col_sets[c].add(num)
                        box_sets[box_idx].add(num)
                        board[r][c] = str(num)
                        
                        backtrack(newR, newC)
                        
                        if not solved:
                            row_sets[r].remove(num)
                            col_sets[c].remove(num)
                            box_sets[box_idx].remove(num)
                            board[r][c] = '.'
                        
        
        backtrack(0, 0)
        return solved