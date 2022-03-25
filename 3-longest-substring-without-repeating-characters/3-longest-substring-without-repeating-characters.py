class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_frequency = {}
        start = 0
        max_len = 0
        
        for end in range(len(s)):
            if s[end] not in char_frequency:
                char_frequency[s[end]] = 0
            char_frequency[s[end]] += 1
            
            while char_frequency[s[end]] > 1:
                left = s[start]
                char_frequency[left] -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len
            