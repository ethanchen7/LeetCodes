class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        node = self.trie
        
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        
        node['finished'] = True

    def search(self, word: str) -> bool:
        
        def dfs(word, node):
            for i, char in enumerate(word):
                if char not in node:
                    if char == ".":
                        for c in node:
                            if c != 'finished' and dfs(word[i+1:], node[c]): # ignore the "." and advance the node forward /
                                # and we also decrease the word size
                                return True
                    return False
                else:
                    node = node[char]
            
            return 'finished' in node
        
        return dfs(word, self.trie)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)