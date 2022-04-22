class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        char_frequency = {}
        matched = 0
        start = 0
        
        # first, add all the characters to the hashmap
        for char in s1:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        
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
            
            if matched == len(char_frequency):
                return True
        
        return False
                