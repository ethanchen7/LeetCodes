class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        graph = collections.defaultdict(list)
        
        for word in wordList:
            chars = list(word)
            for j in range(len(word)):
                pattern = chars[:]
                pattern[j] = "*"
                graph["".join(pattern)].append(word)
        
        queue = collections.deque()
        queue.append((beginWord, 0))
        visited = set()
        
        while queue:
            
            word, step = queue.popleft()
            
            if word == endWord:
                return step + 1
            
            if word not in visited:
                visited.add(word)
                
                chars = list(word)
                for j in range(len(word)):
                    pattern = chars[:]
                    pattern[j] = "*"
                    for w in graph["".join(pattern)]:
                        if w not in visited:
                            queue.append((w, step + 1))
        return 0