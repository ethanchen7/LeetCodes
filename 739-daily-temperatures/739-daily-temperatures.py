class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        
        stack = deque()
        for next_idx, next_temp in enumerate(temperatures):
            while stack and stack[-1][1] < next_temp:
                prev_idx, prev_temp = stack.pop()
                res[prev_idx] = (next_idx - prev_idx)
            
            stack.append((next_idx, next_temp))
        
        return res