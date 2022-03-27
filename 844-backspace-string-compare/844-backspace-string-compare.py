class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index1 = len(s) - 1
        index2 = len(t) - 1
        
        while (index1 >= 0 or index2 >= 0):
            
            i1 = self.get_valid_char_idx(s, index1)
            i2 = self.get_valid_char_idx(t, index2)
            
            if i1 < 0 and i2 < 0:
                return True # if both reach the end of the strings
            
            if i1 < 0 or i2 < 0:
                return False # if only one of the strings reach the end
            
            if s[i1] != t[i2]:
                return False
            
            index1 = i1 - 1
            index2 = i2 - 1
        
        return True # if both hit zero
            
    
    def get_valid_char_idx(self, stri, index):
        
        backspaces = 0
        
        while index >= 0:
            if stri[index] == "#":
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                break
        
            index -= 1
        
        return index