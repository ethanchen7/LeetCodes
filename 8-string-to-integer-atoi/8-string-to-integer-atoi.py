class Solution:
    def myAtoi(self, s: str) -> int:
        
        upper_bound = pow(2,31) - 1
        lower_bound = -pow(2,31)
        n = len(s)
        
        stripped = s.strip()
        result = 0
        isNegative = False
        
        index = 0
        while index < n and s[index] == ' ':
            index += 1
        
        if index < n and s[index] == "-":
            isNegative = True
            index += 1
        
        elif index < n and s[index] == "+":
            isNegative = False
            index += 1
        
        while index < n and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
            
            if result < lower_bound:
                return lower_bound if isNegative == False else upper_bound
            
            elif result > upper_bound:
                return upper_bound if isNegative == False else lower_bound
            
        if isNegative:
            result *= -1
        
        return result
        
        