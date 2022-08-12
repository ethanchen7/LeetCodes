class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        rs = set()
        cs = set()
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rs.add(r)
                    cs.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in rs or c in cs:
                    matrix[r][c] = 0