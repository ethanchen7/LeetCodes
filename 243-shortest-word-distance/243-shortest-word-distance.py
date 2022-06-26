class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        index1 = -1
        index2 = -1
        min_distance = math.inf
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                index1 = i
            elif wordsDict[i] == word2:
                index2 = i
            
            if index1 != -1 and index2 != -1:
                min_distance = min(abs(index1 - index2), min_distance)
            
        return min_distance
                
            