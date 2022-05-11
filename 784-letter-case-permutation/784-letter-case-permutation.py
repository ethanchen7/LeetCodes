class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        permutations = []
        permutations.append(s)
        
        for i in range(len(s)):
            
            if s[i].isalpha():
                
                n = len(permutations)
                for j in range(n):
                    chars = list(permutations[j])
                    chars[i] = chars[i].swapcase()
                    permutations.append(''.join(chars))
        
        return permutations