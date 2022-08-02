class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for i in range(len(asteroids)):
            
            stack.append(asteroids[i])
            
            while len(stack) >= 2:
                colliding = (stack[-1] < 0 and stack[-2] > 0)
                if colliding:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if abs(num1) > abs(num2):
                        stack.append(num1)
                    elif abs(num2) > abs(num1):
                        stack.append(num2)

                else:
                    break
                
        
        return stack
            