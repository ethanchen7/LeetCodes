class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        start = 0
        char_frequency = {}
        matched = 0
        result_indices = []
        
        for char in p: 
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        for end in range(len(s)):
            right = s[end]
            if right in char_frequency:
                char_frequency[right] -= 1
                if char_frequency[right] == 0:
                    matched += 1
            
            if matched == len(char_frequency):
                result_indices.append(start)
            
            if end - start + 1 >= len(p):
                left = s[start]
                start += 1
                if left in char_frequency:
                    if char_frequency[left] == 0:
                        matched -= 1
                    char_frequency[left] += 1
            
        return result_indices