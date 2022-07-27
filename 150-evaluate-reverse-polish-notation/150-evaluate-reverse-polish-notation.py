import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = {'+':True, '/':True,'*':True, '-':True}
        
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(token)
            
            else:
                if len(stack) >= 2:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    
                    number = None
                    if token == "+":
                        number = num1 + num2
                    
                    elif token == "-":
                        number = num2 - num1
                    
                    elif token == "*":
                        number = num1 * num2
                    
                    else:
                        number = num2 / num1
                        if number < 0:
                            number = math.ceil(number)
                        else:
                            number = math.floor(number)
                    
                    stack.append(number)
            
        return stack[0]
            