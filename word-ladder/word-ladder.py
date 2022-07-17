class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        graph = collections.defaultdict(list)
        
        for word in wordList:
            chars = list(word)
            for i in range(len(word)):
                pattern = chars[:]
                pattern[i] = "*"
                graph["".join(pattern)].append(word)
        
        queue = collections.deque()
        visited = set()
        queue.append((beginWord, 0))
        
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step + 1
            
            if word not in visited:
                visited.add(word)
                
                chars = list(word)
                for i in range(len(word)):
                    pattern = chars[:]
                    pattern[i] = "*"
                    for w in graph["".join(pattern)]:
                        if w not in visited:
                            queue.append((w, step + 1))
        return 0
                            