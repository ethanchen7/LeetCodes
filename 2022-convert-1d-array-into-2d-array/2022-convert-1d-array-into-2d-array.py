class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        result = []
        
        length = len(original)
        if m * n != length:
            return result
        
        index = 0
        for c in range(m):
            row = []
            
            while True:
                row.append(original[index])
                index += 1
                if index % n == 0:
                    result.append(row)
                    break
        
        return result