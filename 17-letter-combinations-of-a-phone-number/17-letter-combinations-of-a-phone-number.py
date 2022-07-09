class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        digit_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
            
        if not digits:
            return None
        result = []
        sub = []
        
        def dfs(idx,sub):
            
            if len(sub) == len(digits):
                result.append("".join(sub))
                return
            
            possible_letters = digit_map[digits[idx]]
            for letter in possible_letters:
                sub.append(letter)
                dfs(idx + 1, sub)
                sub.pop()
            
        dfs(0,sub)
        return result
        
            