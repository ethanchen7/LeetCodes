class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = {}
        inDegrees = {}
        
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = []
                    inDegrees[char] = 0
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                char1, char2 = word1[j], word2[j]
                if char1 != char2:
                    graph[char1].append(char2)
                    inDegrees[char2] += 1
                    break
            
            else:
                if len(word2) < len(word1):
                    return ""
        
        sources = deque()
        for key in inDegrees:
            if inDegrees[key] == 0:
                sources.append(key)
        
        sorted_order = []
        while sources:
            char = sources.popleft()
            sorted_order.append(char)
            for c in graph[char]:
                inDegrees[c] -= 1
                if inDegrees[c] == 0:
                    sources.append(c)
        
        if len(sorted_order) != len(inDegrees):
            return ""
        
        return "".join(sorted_order)