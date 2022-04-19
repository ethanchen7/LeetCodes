class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_chars = set()
        for char in allowed:
            allowed_chars.add(char)
        
        count = 0
        for word in words:
            valid = True
            for letter in word:
                if letter not in allowed_chars:
                    valid = False
            
            if valid:
                count += 1
                
        
        return count