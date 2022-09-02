class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if (m * n) != len(original):
            return []
        
        result = []
        i = 0
        for _ in range(m):
            temp = []
            for _ in range(n):
                temp.append(original[i])
                i += 1
            result.append(temp)
        return result
        