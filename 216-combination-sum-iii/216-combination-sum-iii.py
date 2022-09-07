class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        
        def dfs(i, numbers, total):
            
            if total == n and len(numbers) == k:
                result.append(numbers[:])
                return
            
            if len(numbers) > k or total > n:
                return
            
            for j in range(i + 1, 10):
                dfs(j, numbers + [j], total + j)
        
        dfs(0, [], 0)
        return result