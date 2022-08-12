class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for i in range(len(s)):
            char = s[i]

            if char != ']':
                stack.append(char)
            
            else:
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop() # pop off the [
                
                multiplier = ""
                while stack and stack[-1].isnumeric():
                    multiplier = stack.pop() + multiplier
                
                result = string * int(multiplier)
                stack.append(result)
                
        return "".join(stack)