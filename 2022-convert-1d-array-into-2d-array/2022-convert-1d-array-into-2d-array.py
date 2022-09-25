class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        
        if (m * n) != len(original):
            return None
        
        result = []
        
        i = 0
        while i < len(original):
            result.append(original[i: i + n])
            i += n
        
        return result