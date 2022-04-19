class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        res = [word for word in s.split(' ') if word != ""]
        return len(res[-1])