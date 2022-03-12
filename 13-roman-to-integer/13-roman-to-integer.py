class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        if not s:
            return 0
        
        total = roman[s[-1]]
        
        N = len(s) - 2
        
        while N >= 0:
            
            if roman[s[N]] < roman[s[N + 1]]:
                total -= roman[s[N]]
            
            else:
                total += roman[s[N]]
            
            N -= 1
        
        return total
    
    