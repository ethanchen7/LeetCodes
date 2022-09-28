class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = collections.defaultdict(list)
        wordList.append(beginWord)
        visited = set()
        
        for word in wordList:
            for i in range(len(word)):
                copy = list(word)
                copy[i] = '*'
                graph["".join(copy)].append(word)
        
        time = 0
        queue = deque()
        queue.append([beginWord, time])
    
        while queue:

            word, time = queue.popleft()

            if word in visited:
                continue

            if word == endWord:
                return time + 1
            
            visited.add(word)

            for i in range(len(word)):
                chars = list(word)
                chars[i] = '*'
                for wrd in graph["".join(chars)]:
                    if wrd not in visited:
                        queue.append([wrd, time + 1])
                        

        return 0
            
    def options(self, word):
        options = []
        for i in range(len(word)):
            copy = list(word)
            copy[i] = '*'
            options.append("".join(copy))
        return options