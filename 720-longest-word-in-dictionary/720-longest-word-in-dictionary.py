class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key=lambda x: (x, -len(x)), reverse=True)
        words_set = set(words)
      
        trie = {}
        for word in words_set:
            root = trie
            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]
            root['$'] = word

        queue = deque([trie]) # bfs the trie
        res = ""
        while queue:
            
            node = queue.popleft()
            for c in node.values():
                if '$' in c:
                    queue.append(c)
                
                    word = c['$']
                    if len(word) > len(res) or word < res: # if it's lexicographically smaller
                        res = word
        return res
                
        
        