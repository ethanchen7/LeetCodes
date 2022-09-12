class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        root = self.trie
        
        for char in word:
            if char not in root:
                root[char] = {}
            
            root = root[char]
        
        root['$'] = word

    def search(self, word: str) -> bool:
        
        root = self.trie
        
        for char in word:
            if char not in root:
                return False
            root = root[char]
        
        return '$' in root and root['$'] == word
        

    def startsWith(self, prefix: str) -> bool:
        
        root = self.trie
        
        for char in prefix:
            if char not in root:
                return False
            root = root[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)