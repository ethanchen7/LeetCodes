class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        def dfs(curr, total, numbers):
            
            if total == n and len(numbers) == k:
                result.append(numbers[:])
                return
            
            elif total > n or len(numbers) >= k:
                return
            
            for i in range(curr, 9):
                
                numbers.append(i+1) # starts at 0
                dfs(i + 1, total + i + 1, numbers)
                numbers.pop()
 
        dfs(0, 0, [])
        return result