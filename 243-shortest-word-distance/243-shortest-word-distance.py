class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        word_indices = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] not in word_indices:
                word_indices[wordsDict[i]] = []
            word_indices[wordsDict[i]].append(i)
        
        min_len = math.inf
        for j in word_indices[word1]:
            for z in word_indices[word2]:
                min_len = min(abs(j-z), min_len)
        
        return min_len
            