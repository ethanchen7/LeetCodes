class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        
        while i >= 0:
            
            if digits[i] != 9:
                digits[i] += 1
                break
            
            else:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0,1)
                else:
                    digits[i] = 0
            
            i -= 1
        
        return digits
                    
                    