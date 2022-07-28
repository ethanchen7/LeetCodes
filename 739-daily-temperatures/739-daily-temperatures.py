class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        
        stack = []
        
        for i, temp in enumerate(temperatures):
            
            if stack:
                while stack and stack[-1][1] < temp:
                    old_idx, old_temp = stack.pop()
                    res[old_idx] = i - old_idx
            
            stack.append([i, temp])
        
        return res