class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        start, matched = 0, 0
        min_length = len(s) + 1
        char_frequency = {}
        
        for char in t:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        for end in range(len(s)):
            right_char = s[end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] >= 0:
                    matched += 1
            
            while matched == len(t):
                
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    substr_start = start
                
                left_char = s[start]
                start += 1
                
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1
        
        if min_length == len(s) + 1:
            return ''
        
        return s[substr_start:substr_start + min_length]