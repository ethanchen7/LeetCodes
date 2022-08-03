class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()
        # [1, 1, 2, 5, 6, 7, 10]
        
        def backtrack(i, total, numbers):
            
            if total == target:
                result.append(numbers[:])
                return
            
            if total > target or i >= len(candidates):
                return
            
            prev = -1
            for j in range(i, len(candidates)): 
            
                if prev == candidates[j]:
                    continue
                numbers.append(candidates[j])
                prev = candidates[j]
                backtrack(j + 1, total + candidates[j], numbers)
                numbers.pop()
    
        backtrack(0, 0, [])
        return result