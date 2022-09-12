class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        
        def dfs(total, combo, i):

            if len(combo) == k:
                if total == n:
                    result.append(combo[:])
                    return
            
            if len(combo) > k or total > n:
                return
            
            for j in range(i + 1, 10):
                
                combo.append(j)
                total += j
                
                dfs(total, combo, j)
                
                combo.pop()
                total -= j
        
        dfs(0, [], 0)
        return result
            
            