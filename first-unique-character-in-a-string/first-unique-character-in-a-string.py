class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_frequency = {}
        
        for char in s:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        for i in range(len(s)):
            if char_frequency[s[i]] == 1:
                return i
        
        return -1