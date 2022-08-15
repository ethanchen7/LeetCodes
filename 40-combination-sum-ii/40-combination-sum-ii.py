class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    
        
        result = []
        numbers = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        # [(10, 1), (1, 2), (2, 1), (7, 1), (6, 1), (5, 1)]
        
        def dfs(idx, total, numbers):
            
            if total == target:
                result.append(numbers[:])
                return
            
            elif total > target:
                return
            
            for i in range(idx, len(counter)): # loop through the counter
                
                candidate, freq = counter[i]
                
                if freq <= 0:
                    continue 
                    
                numbers.append(candidate)
                counter[i] = (candidate, freq - 1) # decrement the frequency
                
                dfs(i, total + candidate, numbers) # search the rest of the numbers
                
                counter[i] = (candidate, freq) # backtrack
                numbers.pop()
        
        dfs(0, 0, numbers)
        return result