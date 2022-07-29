class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(len(board))]
        cols = [set() for j in range(len(board[0]))]
        boxes = [set() for x in range(len(board))]
        
        ROW = len(board)
        COL = len(board[0])
        
        for r in range(ROW):
            for c in range(COL):
                
                num = board[r][c]
                
                if num == '.':
                    continue
                
                if num in rows[r]:
                    return False
                
                rows[r].add(num)
                
                if num in cols[c]:
                    return False
                    
                cols[c].add(num)
                
                box_idx = r // 3 * 3 + c // 3
                if num in boxes[box_idx]:
                    return False
                boxes[box_idx].add(num)
        
        return True