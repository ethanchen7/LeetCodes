class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort()
        
        stack = []
        for p, s in pairs[::-1]:
            time = (target - p) / s
            stack.append(time)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)