class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        outerLeft = 0
        outerRight = len(matrix) - 1
        
        while outerLeft <= outerRight:
            
            mid = (outerLeft + outerRight) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]: # target is in this box
                
                innerLeft, innerRight = 0, len(matrix[mid]) - 1
                while innerLeft <= innerRight:
                    innerMid = (innerLeft + innerRight) // 2
                    if target == matrix[mid][innerMid]:
                        return True
                    
                    elif matrix[mid][innerMid] < target:
                        innerLeft = innerMid + 1
                    
                    else:
                        innerRight = innerMid - 1
                return False
            
            elif target > matrix[mid][-1]:
                outerLeft = mid + 1
            
            else:
                outerRight = mid - 1
        
        return False