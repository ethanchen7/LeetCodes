class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         length = len(digits)
#         i = length - 1 # start in the back
        
#         while i >= 0:
            
#             #check for 9s
#             if digits[i] == 9:
#                 if i == 0:
#                     digits[i] = 0
#                     digits.insert(0, 1)
#                 else:
#                     digits[i] = 0
#             else:
#                 digits[i] += 1
#                 break # exit the loop if no 9s
#             i-=1
#         return digits
            
            
        i = len(digits) - 1
        
        while i >= 0:
            
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                else:
                    digits[i] = 0
            else:
                digits[i] += 1
                break
            
            i-=1
        return digits
            
            
            
        
        