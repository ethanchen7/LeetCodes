class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_repeating_char = 0
        start = 0
        char_freq = {}
        max_length = 0
        
        for end in range(len(s)):
            right = s[end]
            if right not in char_freq:
                char_freq[right] = 0
            char_freq[right] += 1
            
            max_repeating_char = max(max_repeating_char, char_freq[right])
            
            while (end - start + 1) - max_repeating_char > k:
                left = s[start]
                char_freq[left] -= 1
                max_repeating_char = max(max_repeating_char, char_freq[left])
                start += 1
            
            max_length = max(end - start + 1, max_length)
        
        return max_length