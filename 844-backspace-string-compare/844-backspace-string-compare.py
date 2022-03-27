class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        index1 = len(s) - 1
        index2 = len(t) - 1
        
        while index1 >= 0 or index2 >= 0:
            
            i1 = self.find_next_valid_char(s, index1)
            i2 = self.find_next_valid_char(t, index2)
            
            if i1 < 0 and i2 < 0:
                return True
            
            if i1 < 0 or i2 < 0:
                return False
            
            if s[i1] != t[i2]:
                return False
            
            index1 = i1 - 1
            index2 = i2 - 1
        
        return True
    
    def find_next_valid_char(self, string, index):
        
        backspaces = 0
        
        while index >= 0:
            if string[index] == "#":
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                break
            
            index -= 1
        
        return index
            