class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_frequency = {}
        start = 0
        max_len = 0
        
        for end in range(0, len(s)):
            
            right = s[end]
            
            if right in char_frequency:
                # move start to one after the index of where that repeated letter first appeared 
                start = max(start, char_frequency[right] + 1)
                
            # store the index of where we last saw the character
            char_frequency[right] = end
                
            #keep track of max length
            max_len = max(max_len, end - start + 1)
        
        return max_len