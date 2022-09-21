class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_frequency = {}
        start = 0
        max_window = 0
        
        for end in range(len(s)):
            right = s[end]
            
            if right not in char_frequency:
                char_frequency[right] = 0
            char_frequency[right] += 1
        
            while char_frequency[right] > 1:
                left = s[start]
                char_frequency[left] -= 1
                if char_frequency[left] == 0:
                    del char_frequency[left]
                start += 1
                
            max_window = max(max_window, end - start + 1)
        
        return max_window
            