class Solution:
    def myAtoi(self, s: str) -> int:
        
        upper_bound = pow(2,31) - 1
        lower_bound = -pow(2,31)
        n = len(s)
        
        isNegative = False
        result = 0
        
        index = 0
        while index < n and s[index] == ' ': # skip all the whitespaces
            index += 1
        
        if index < n and s[index] == '-': # check for negatives
            isNegative = True
            index += 1
        elif index < n and s[index] == "+":
            isNegative = False
            index += 1
        
        while index < n and s[index].isdigit():
            result = result * 10 + int(s[index])
            if result < lower_bound:
                return lower_bound if isNegative == False else upper_bound
            
            elif result > upper_bound:
                return upper_bound if isNegative == False else lower_bound
            
            index += 1
            
        if isNegative:
            return -result
        else:
            return result