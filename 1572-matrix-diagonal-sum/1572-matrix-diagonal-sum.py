class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        rows = len(mat[0])
        cols = len(mat)
        
        i, j = 0, cols - 1
        
        total = 0
        
        for row in mat:
            total += row[i] + row[j]
            i += 1
            j -= 1
            
        # if the len of the matrix is odd, find the middle and subtract it
        if cols % 2 != 0:
            middle = rows // 2
            total -= mat[middle][middle]
            
        return total