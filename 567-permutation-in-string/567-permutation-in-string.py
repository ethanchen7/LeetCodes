class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        start = 0
        matches = 0
        
        char_frequency = {}
        
        
        for char in s1:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        for end in range(len(s2)):
            right = s2[end]
            if right in char_frequency:
                char_frequency[right] -= 1
                if char_frequency[right] == 0:
                    matches += 1
                    
            if matches == len(char_frequency):
                return True
            
            # if the window is too big, shrink it
            if end - start + 1 >= len(s1):
                left = s2[start]
                start += 1
                # if the character was going out of pattern, put it back into the map
                if left in char_frequency:
                    if char_frequency[left] == 0:
                        matches -= 1
                    char_frequency[left] += 1
        
        return False
            