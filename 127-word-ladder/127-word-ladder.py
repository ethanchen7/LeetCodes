class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = collections.defaultdict(list)
        
        for word in wordList:
            i = 0
            
            while i < len(word):
                chars = list(word)
                chars[i] = '*'
                graph["".join(chars)].append(word)
                i += 1
        
        visited = set()
        queue = deque()
        queue.append((beginWord, 1))
        
        while queue:
            
            word, length = queue.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                chars = list(word)
                chars[i] = "*"
                potential_word = "".join(chars)
                
                if potential_word in graph:
                    for wrd in graph[potential_word]:
                        
                        if wrd in visited:
                            continue
                        else:
                            queue.append((wrd, length + 1))
                            visited.add(wrd)
        
        return 0
            
            