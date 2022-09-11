class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        result = []
        
        for i in range(len(text)):
            for word in words:
                if text[i:i + len(word)] == word:
                    result.append([i, i + len(word) - 1])
        
        result.sort()
        return result
            