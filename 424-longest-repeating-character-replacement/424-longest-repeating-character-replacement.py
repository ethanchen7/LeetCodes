class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_repeating_chars = 0
        char_frequency = {}
        max_length = 0
        
        start = 0
        
        for end in range(len(s)):
            right = s[end]
            
            if right not in char_frequency:
                char_frequency[right] = 0
            char_frequency[right] += 1
        
            max_repeating_chars = max(max_repeating_chars, char_frequency[right])
            
            while (end - start + 1 - max_repeating_chars) > k:
                left = s[start]
                char_frequency[left] -= 1
                max_repeating_chars = max(max_repeating_chars, char_frequency[left])
                if char_frequency[left] == 0:
                    del char_frequency[left]
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length