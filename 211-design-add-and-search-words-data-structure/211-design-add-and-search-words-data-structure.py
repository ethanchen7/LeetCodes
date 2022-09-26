class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        root = self.trie
        for char in word:
            if char not in root:
                root[char] = {}
            
            root = root[char]
        
        root['WORD_KEY'] = word

    def search(self, word: str) -> bool:
        
        def dfs(word, root):
            
            for i,char in enumerate(word):
                if char not in root:
                    if char == ".":
                        for node in root:
                            if node != 'WORD_KEY' and dfs(word[i + 1:], root[node]):
                                return True
                    
                    return False
                else:
                    root = root[char]
            
            return 'WORD_KEY' in root
        
        return dfs(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)