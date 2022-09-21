class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        char_frequency = Counter(s1)
        matched = 0
        
        start = 0
        
        for end in range(len(s2)):
            right = s2[end]
            
            if right in char_frequency:
                char_frequency[right] -= 1
                if char_frequency[right] == 0:
                    matched += 1
            
            if (end - start + 1) > len(s1):
                left = s2[start]
                if left in char_frequency:
                    if char_frequency[left] == 0:
                        matched -= 1
                    char_frequency[left] += 1
                start += 1
            
            if (end - start + 1) == len(s1) and matched == len(char_frequency):
                return True
        
        return False
            