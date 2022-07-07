class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = {}
        inDegrees = {}
        
        for word in words:
            for char in word:
                graph[char] = []
                inDegrees[char] = 0
        
        for i in range(0, len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(0, min(len(w1), len(w2))):
                char1, char2 = w1[j], w2[j]
                if char1 != char2:
                    graph[char1].append(char2)
                    inDegrees[char2] += 1
                    break
            else: # why do we write the else here??
                if len(w2) < len(w1): # check that second word isn't a prefix of first word
                    return ""

        sources = collections.deque()
        for key in inDegrees:
            if inDegrees[key] == 0:
                sources.append(key)
        
        sortedOrder = []
        while sources:
            source = sources.popleft()
            sortedOrder.append(source)
            for child in graph[source]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) < len(inDegrees):
            return ""
        
        return "".join(sortedOrder)