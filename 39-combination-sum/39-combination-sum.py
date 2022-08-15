class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        numbers = []
        
        def dfs(idx, total, numbers):
            
            if total == target:
                result.append(numbers[:])
                return
            
            if total > target:
                return
            
            for i in range(idx, len(candidates)):
                numbers.append(candidates[i])
                dfs(i, total + candidates[i], numbers) # search the rest of the numbers starting from that index
                numbers.pop()
            
        dfs(0,0, numbers)
        return result